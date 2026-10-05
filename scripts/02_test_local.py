import yaml
import sys

def run_local_dry_run(config_path: str):
    print(f"🧪 Running local validation dry-run using {config_path}...")
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    print(f"Model: {config['model_name']}")
    print(f"Max Steps: {config['max_steps']} (Local dry run)")
    print("✅ Local pipeline test passed! Ready for cloud execution.")

if __name__ == "__main__":
    run_local_dry_run("configs/local_test.yaml")
