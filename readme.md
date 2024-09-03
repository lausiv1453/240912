# RAG 간단 파이프라인 ㅅㄷ

## 개요

이 프로젝트는 Docker와 Flask를 사용하여 간단한 Retrieval-Augmented Generation (RAG) 파이프라인을 설정합니다. 이 파이프라인은 네 개의 주요 구성 요소로 이루어져 있습니다:

1. **임베딩 모델 서비스**: 입력 쿼리에 대한 임베딩을 생성합니다.
2. **벡터 데이터베이스**: Qdrant를 사용하여 벡터를 저장하고 검색합니다.
3. **프레임워크**: 임베딩 모델, 벡터 데이터베이스 및 LLM 간의 상호 작용을 관리합니다.
4. **LLM 서비스**: 검색된 컨텍스트와 입력 쿼리를 기반으로 응답을 생성합니다.

## 서비스 흐름

1. 사용자가 웹 인터페이스에서 질문을 입력합니다.
2. 프레임워크 서비스가 질문을 임베딩 모델 서비스로 전송하여 임베딩 벡터를 생성합니다.
3. 생성된 임베딩 벡터를 벡터 데이터베이스에서 검색하여 관련 문서들을 찾습니다.
4. 검색된 문서와 원래 질문을 LLM 서비스로 전송하여 최종 응답을 생성합니다.
5. 생성된 응답을 웹 인터페이스에 표시합니다.

## 소스코드 구조

rag-simple-pipeline/
├── embedding_model/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── vector_db/
│   ├── app.py
│   ├── init_db.py
│   ├── Dockerfile
│   └── requirements.txt
├── framework/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── llm/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── README.md



## 설정 및 설치

### 사전 요구 사항

- Docker
- Docker Compose

### 단계

1. **레포지토리 클론**

    ```sh
    git clone https://github.com/unnie7/rag-simple-pipeline.git
    cd rag-simple-pipeline
    ```

2. **Docker 컨테이너 빌드 및 실행**

    ```sh
    docker-compose up --build
    ```

    이 명령어는 `docker-compose.yml` 파일에 정의된 모든 서비스를 빌드하고 시작합니다.

3. **벡터 데이터베이스 초기화**

    벡터 데이터베이스 (`vector_db`)는 시작 시 자동으로 샘플 데이터로 초기화됩니다.

## 서비스

### 임베딩 모델 서비스

- **엔드포인트**: `/embed`
- **메소드**: `POST`
- **요청 본문**:
    ```json
    {
        "sentences": ["여기에 당신의 쿼리를 입력하세요"]
    }
    ```
- **응답**:
    ```json
    [
        [0.1, 0.2, 0.3, ...]
    ]
    ```

### 프레임워크

- **엔드포인트**: `/query`
- **메소드**: `POST`
- **요청 본문**:
    ```json
    {
        "query": "여기에 질문을 입력하세요"
    }
    ```
- **응답**: 벡터 데이터베이스에서 상위 5개의 검색 결과를 포함한 JSON.

### LLM 서비스

- **엔드포인트**: `/generate`
- **메소드**: `POST`
- **요청 본문**:
    ```json
    {
        "prompt": "여기에 프롬프트를 입력하세요"
    }
    ```
- **응답**:
    ```json
    {
        "response": "생성된 응답이 여기에 표시됩니다"
    }
    ```

## 사용법

- 프레임워크 서비스를 `http://localhost:5000`에서 액세스할 수 있습니다.
