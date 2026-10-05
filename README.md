Markdown
# ⚡ Hybrid AI Lab: Local Prototyping & Cloud-Burst Fine-Tuning Pipeline

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework: PyTorch / Unsloth](https://img.shields.io/badge/Framework-PyTorch%20%2F%20Unsloth-red.svg)](https://github.com/unslothai/unsloth)
[![Platform: Apple MLX / CUDA / ROCm](https://img.shields.io/badge/Platform-Metal%20%2F%20CUDA%20%2F%20ROCm-green.svg)](#architecture-overview)

A lightweight, budget-friendly blueprint for developing, instructing, and fine-tuning Large Language Models (LLMs). This architecture maximizes efficiency by running **80% of development locally** ($0/hr iteration) and bursting to **cloud GPU pods for 20% heavy gradient training**.

---

## 📌 Table of Contents
- [Architecture Overview](#-architecture-overview)
- [Why Hybrid? (Cost & Efficiency)](#-why-hybrid-cost--efficiency)
- [Directory Structure](#-directory-structure)
- [Prerequisites & Setup](#-prerequisites--setup)
- [Quickstart Workflow](#-quickstart-workflow)
  - [Phase 1: Local Data Prep & 100-Sample Test](#phase-1-local-data-prep--100-sample-test)
  - [Phase 2: Ephemeral Cloud Fine-Tuning](#phase-2-ephemeral-cloud-fine-tuning)
  - [Phase 3: Local Pull, Quantization & Evaluation](#phase-3-local-pull-quantization--evaluation)
- [Supported Environments](#-supported-environments)
- [Contributing & License](#-contributing--license)

---

## 🏗️ Architecture Overview

                  ┌─────────────────────────────────────────┐
                  │          LOCAL ON-PREMISE NODE          │
                  │   (Apple Silicon / RTX / AMD Strix)     │
                  ├─────────────────────────────────────────┤
                  │ • Dataset Filtering & Tokenization      │
                  │ • Prompt Engineering & Synthetic Data   │
                  │ • QLoRA Pipeline Validation (100 rows)  │
                  │ • Quantized Offline Inference & Eval    │
                  └────────────────────┬────────────────────┘
                                       │
                    Git / Hugging Face Hub / WandB Sync
                                       │
                  ┌────────────────────▼────────────────────┐
                  │         HYBRID CLOUD BURST NODE         │
                  │   (RunPod / Lambda / Modal / Vast)      │
                  ├─────────────────────────────────────────┤
                  │ • Full Epoch Multi-GPU Fine-Tuning      │
                  │ • DeepSpeed / FlashAttention-2 / Unsloth│
                  │ • Automatic Model Checkpoint Push       │
                  │ • Auto-termination upon completion     │
                  └─────────────────────────────────────────┘

---

## 💡 Why Hybrid? (Cost & Efficiency)

Developing AI strictly in the cloud leads to massive idle spending during debugging, dataset formatting, and output evaluation.

| Task Phase | Traditional Cloud-Only Cost | Hybrid Architecture Cost |
| :--- | :--- | :--- |
| **Data Cleaning & Pipeline Debugging (20 hrs)** | ~$2.50/hr = **$50.00** | **$0.00** *(Runs locally)* |
| **Full Model Training (5 hrs)** | ~$2.50/hr = **$12.50** | **$12.50** *(Bursts on-demand)* |
| **Inference, Testing & Benchmarking (30 hrs)** | ~$1.50/hr = **$45.00** | **$0.00** *(Runs locally via Ollama/GGUF)* |
| **TOTAL PER EXPERIMENT RUN** | **$107.50** | **$12.50** *(88% Cost Reduction)* |

---

## 📂 Directory Structure

```text
hybrid-ai-lab/
├── .github/                  # CI/CD & Automated Cloud Launch Actions
├── configs/                  # Training Hyperparameters & Quantization Settings
│   ├── local_test.yaml       # Fast 100-sample CPU/Metal/iGPU config
│   └── cloud_full.yaml       # Multi-GPU / High-VRAM Full Training config
├── data/                     # Raw & Formatted Datasets (Git-ignored)
│   ├── raw/                  # Ingested jsonl / parquet files
│   └── processed/            # Tokenized instruction datasets
├── scripts/                  # Workflow Execution Scripts
│   ├── 01_prep_dataset.py    # Local dataset filtering & formatting
│   ├── 02_test_local.py      # Dry-run training locally (1-2 steps)
│   ├── 03_cloud_train.py     # Main cloud training script (PyTorch/Unsloth)
│   └── 04_merge_quantize.py  # Merge LoRA adapters & export GGUF/MLX
├── requirements.txt          # Python dependencies
└── README.md                 # Project Documentation
🛠️ Prerequisites & Setup
1. Local Environment Setup
Clone the repository and set up a virtual environment on your local machine (Mac, Windows, or Linux):

Bash
git clone [https://github.com/your-username/hybrid-ai-lab.git](https://github.com/your-username/hybrid-ai-lab.git)
cd hybrid-ai-lab

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
2. Configure Environment Keys
Create a .env file in the root directory:

Bash
HUGGING_FACE_HUB_TOKEN="hf_your_token_here"
WANDB_API_KEY="your_wandb_key_here"
🚀 Quickstart Workflow
Phase 1: Local Data Prep & 100-Sample Test
Prepare your instruction dataset and run a 2-step training validation locally to confirm there are no syntax errors or Out-Of-Memory (OOM) crashes before paying for cloud compute.

Bash
# Step 1: Format & Tokenize Dataset
python scripts/01_prep_dataset.py --dataset_name "your-raw-data.jsonl"

# Step 2: Run Local Validation Test (Executes 2 steps on 100 sample rows)
python scripts/02_test_local.py --config configs/local_test.yaml
If 02_test_local.py completes without error, your code and dataset are verified for cloud deployment.

Phase 2: Ephemeral Cloud Fine-Tuning
Launch a cloud GPU instance (e.g., RunPod, Lambda Labs, or Modal), clone your repository, and trigger the full training run.

Bash
# On your Cloud GPU Pod terminal:
git clone [https://github.com/your-username/hybrid-ai-lab.git](https://github.com/your-username/hybrid-ai-lab.git)
cd hybrid-ai-lab && pip install -r requirements.txt

# Run Full Fine-Tuning Session
python scripts/03_cloud_train.py \
    --config configs/cloud_full.yaml \
    --push_to_hub \
    --repo_id "your-username/my-finetuned-model"
Note: The cloud script automatically pushes trained LoRA adapters directly to Hugging Face Hub upon completion, preventing data loss if the cloud instance terminates.

Phase 3: Local Pull, Quantization & Evaluation
Download your trained LoRA weights locally, merge them with the base model, convert them to GGUF or MLX format, and run local evaluation offline.

Bash
# Step 1: Pull LoRA Weights & Convert to GGUF/MLX
python scripts/04_merge_quantize.py \
    --repo_id "your-username/my-finetuned-model" \
    --format "gguf" \
    --quant_type "q4_k_m"

# Step 2: Run Local Ollama / vLLM Server for Evaluation
ollama create my-custom-model -f Modelfile
ollama run my-custom-model "Explain the core concepts of my fine-tuned dataset."
💻 Supported Local Environments
This pipeline is optimized out-of-the-box for diverse local developer setups:

Apple Silicon (M1/M2/M3/M4/M5 Max & Ultra): Native Metal acceleration via Apple MLX & PyTorch MPS backend.

NVIDIA Local GPUs (RTX 3000/4000/5000 Series): Full CUDA support with 4-bit/8-bit QLoRA via bitsandbytes and Unsloth.

AMD APUs & GPUs (Strix Halo / RX Series): Native Linux ROCm support for open-source PyTorch execution.

🤝 Contributing & License
Contributions are welcome! Feel free to open an Issue or Pull Request to add new local quantization formats or cloud provider templates.

This project is licensed under the MIT License — see the LICENSE file for details.
