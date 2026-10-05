import os
import sys
from security.guardrail_check import sanitize_input

def process_dataset(input_file: str, output_file: str):
    print(f"🔒 Processing and sanitizing dataset: {input_file}")
    if not os.path.exists(input_file):
        print(f"Creating placeholder sample in {input_file} for testing...")
        os.makedirs(os.path.dirname(input_file), exist_ok=True)
        with open(input_file, "w") as f:
            f.write('{"prompt": "Explain neural networks", "response": "Neural networks are compute graphs."}\n')

    sanitized_count = 0
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            check = sanitize_input(line)
            if check["is_safe"]:
                outfile.write(line)
                sanitized_count += 1
            else:
                print(f"⚠️ Row dropped due to security violation: {check['violations']}")
                
    print(f"✅ Dataset sanitized! Saved {sanitized_count} clean samples to {output_file}")

if __name__ == "__main__":
    process_dataset("data/raw/train_raw.jsonl", "data/processed/train_sanitized.jsonl")
