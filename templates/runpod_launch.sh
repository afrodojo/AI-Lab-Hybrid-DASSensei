#!/bin/bash
echo "🚀 Initializing RunPod Cloud Node..."

# 1. Update & clone repo
git clone https://github.com/YOUR-USERNAME/hybrid-ai-lab.git
cd hybrid-ai-lab

# 2. Install dependencies
pip install -r requirements.txt

# 3. Load HuggingFace token from environment
if [ -z "$HUGGING_FACE_HUB_TOKEN" ]; then
    echo "⚠️ Warning: HUGGING_FACE_HUB_TOKEN is not set."
else
    huggingface-cli login --token $HUGGING_FACE_HUB_TOKEN
fi

# 4. Execute Cloud Training Pipeline
python scripts/03_cloud_train.py --config configs/cloud_full.yaml
