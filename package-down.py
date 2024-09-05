import os

# 패키지를 저장할 디렉토리 생성
os.makedirs('packages', exist_ok=True)

# 임베딩 모델 다운로드
print("Downloading embedding model...")
os.system("wget -P packages https://huggingface.co/sentence-transformers/bert-base-nli-mean-tokens/resolve/main/pytorch_model.bin")

# LLM 모델 다운로드
print("Downloading LLM model...")
os.system("wget -P packages https://huggingface.co/gpt2/resolve/main/pytorch_model.bin")

# PyTorch 패키지 다운로드
print("Downloading PyTorch package...")
os.system("wget -P packages https://download.pytorch.org/whl/cu118/torch-2.0.1+cu118-cp39-cp39-linux_x86_64.whl")

# Transformers 패키지 다운로드
print("Downloading Transformers package...")
os.system("wget -P packages https://files.pythonhosted.org/packages/61/21/6ea1b9aa12a03a3ae7b8d7ed8c0a4f34e54a5b6c1a917b1a9e8b8edc1c7f/transformers-4.30.2-py3-none-any.whl")

# requirements.txt에 필요한 패키지 다운로드
print("Downloading requirements packages...")
os.system("pip download -r embedding_model/requirements.txt -d packages")
os.system("pip download -r vector_db/requirements.txt -d packages")
os.system("pip download -r framework/requirements.txt -d packages")
os.system("pip download -r llm/requirements.txt -d packages")

print("All packages downloaded successfully.")

