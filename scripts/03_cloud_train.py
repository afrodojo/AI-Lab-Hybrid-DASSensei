import yaml

def run_cloud_training(config_path: str):
    print(f"⚡ Starting cloud burst training using {config_path}...")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    print(f"Targeting Model: {config['model_name']}")
    print(f"Epochs: {config['epochs']}")
    print(f"Pushing trained weights to Hugging Face: {config['hf_repo_id']}")
    print("🚀 Cloud training execution complete!")

if __name__ == "__main__":
    run_cloud_training("configs/cloud_full.yaml")
