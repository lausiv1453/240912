# 베이스 이미지를 설정합니다.
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지를 설치합니다.
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# pip 업데이트
RUN pip install --upgrade pip

# requirements.txt 파일을 복사하고 패키지를 설치합니다.
COPY requirements.txt .

# PyTorch CPU 버전을 명시적으로 설치
RUN pip install torch==2.0.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

# 나머지 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 코드 파일을 복사합니다.
COPY . .

# Flask 서버 실행
CMD ["python", "app.py"]
