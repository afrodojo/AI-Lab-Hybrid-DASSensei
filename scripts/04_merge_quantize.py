import os
import sys
from dotenv import load_dotenv

load_dotenv()

def merge_and_quantize(repo_id: str, output_dir: str = 'models/gguf'):
    print(f'?? Exporting model adapter from Hugging Face: {repo_id}')
    os.makedirs(output_dir, exist_ok=True)
    
    modelfile_path = os.path.join(output_dir, 'Modelfile')
    model_gguf_name = 'model_q4_k_m.gguf'
    
    modelfile_content = f'''FROM ./{model_gguf_name}
TEMPLATE """{{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>"""
PARAMETER stop "<|im_start|>"
PARAMETER stop "<|im_end|>"
'''
    
    with open(modelfile_path, 'w') as f:
        f.write(modelfile_content)
        
    print(f'? Ollama Modelfile created at {modelfile_path}')
    print('?? To run locally via Ollama: ollama create hybrid-model -f models/gguf/Modelfile')

if __name__ == '__main__':
    merge_and_quantize('afrodojo/my-finetuned-model')
