# LLM CUDA 기반 API 서버 설치 및 실행 안내

## 1. 개요
이 프로젝트는 CUDA 기반의 AI 추론을 위한 API 서버를 제공합니다. 
Flask 서버를 통해 벡터 덧셈을 GPU에서 수행하고, 이를 API 형태로 제공합니다.

## 2. 요구 사항
- NVIDIA GPU (CUDA 12.2 이상)
- Python 3.7 ~ 3.11
- Docker 및 Docker-Compose

## 3. 설치 방법

### 3.1 패키지 설치
패키지들은 수동으로 다운로드하거나 자동으로 설치할 수 있습니다.

#### 3.1.1 수동 패키지 다운로드
수동으로 다운로드해야 할 패키지는 다음과 같습니다:
- Python
- Docker-Compose
- Qdrant Client
- Setuptools (distutils 대체)

수동 다운로드는 `package-down.py` 스크립트를 통해 수행됩니다. 
수동 설치 패키지는 `hand-packages` 폴더에 저장됩니다.

```bash
python3 package-down.py
