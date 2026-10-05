import modal

app = modal.App("hybrid-ai-lab-trainer")

image = (
    modal.Image.debian_slim(python_version="3.10")
    .pip_install(
        "torch>=2.2.0",
        "transformers",
        "datasets",
        "unsloth",
        "peft",
        "triton",
        "huggingface_hub"
    )
)

@app.function(
    image=image,
    gpu="A100",
    timeout=3600,
    secrets=[modal.Secret.from_name("huggingface-secret")]
)
def train_remote():
    import subprocess
    print("⚡ Modal Cloud Burst Active: Executing fine-tuning job...")
    subprocess.run(["python", "scripts/03_cloud_train.py", "--config", "configs/cloud_full.yaml"])

if __name__ == "__main__":
    with app.run():
        train_remote.remote()
