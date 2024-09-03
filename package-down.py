import os
import subprocess

# 모델 및 패키지 다운로드 경로
package_path = "./package"
embedding_model_path = os.path.join(package_path, "ko-sentence-bert-model")
llm_model_path = os.path.join(package_path, "kogpt2-model")

# 필요한 디렉토리 생성
os.makedirs(package_path, exist_ok=True)
os.makedirs(embedding_model_path, exist_ok=True)
os.makedirs(llm_model_path, exist_ok=True)

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

print("Downloading embedding model...")
# 임베딩 모델 다운로드 (예: Ko-SentenceBERT)
run_command([
    "git",
    "clone",
    "https://huggingface.co/sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens",
    embedding_model_path
])

print("Downloading LLM model...")
# LLM 모델 다운로드 (예: KoGPT2)
run_command([
    "git",
    "clone",
    "https://huggingface.co/taeminlee/kogpt2",
    llm_model_path
])

# PyTorch 다운로드
print("Downloading PyTorch package...")
run_command([
    "wget",
    "https://download.pytorch.org/whl/cu118/torch-2.0.1+cu118-cp39-cp39-linux_x86_64.whl",
    "-O",
    f"{package_path}/torch-2.0.1+cu118-cp39-cp39-linux_x86_64.whl"
])

# Transformers 다운로드
print("Downloading Transformers package...")
run_command([
    "wget",
    "https://files.pythonhosted.org/packages/ce/0a/2e52e9e23ea4c86ef7e6ec13dfdc15d295c0b66fba4f6074ed4ad4450d8e/transformers-4.30.2-py3-none-any.whl",
    "-O",
    f"{package_path}/transformers-4.30.2-py3-none-any.whl"
])
