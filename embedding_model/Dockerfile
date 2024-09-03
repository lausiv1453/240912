# 베이스 이미지
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 및 모델 복사
COPY ./package /app/package
COPY ./package/ko-sentence-bert-model /app/models/embedding_model

# 필요한 패키지 설치
RUN pip install --no-cache-dir /app/package/torch-1.10.0+cu113-cp39-cp39-linux_x86_64.whl \
    /app/package/transformers-4.10.0-py3-none-any.whl

# 모델 실행 또는 초기화에 필요한 추가 명령어
# 예: CMD ["python", "run_embedding.py"]
