from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams
import numpy as np

# Qdrant 클라이언트 연결
client = QdrantClient(host='localhost', port=6333)

# 컬렉션 이름 설정
collection_name = "my_collection"

# 기존 컬렉션 삭제
try:
    client.delete_collection(collection_name)
    print(f"'{collection_name}' 컬렉션이 삭제되었습니다.")
except Exception as e:
    print(f"컬렉션 삭제 중 오류 발생: {e}")

# 벡터 크기를 임베딩 모델에 맞춰 384차원으로 설정
embedding_size = 384

# 384차원 벡터를 지원하는 새로운 컬렉션 생성
client.create_collection(
    collection_name=collection_name,
    vectors_config=VectorParams(size=embedding_size, distance="Cosine")
)

# 초기 데이터 삽입
data = [
    {"conversation_id": "1", "sender": "customer", "message": "안녕하세요, 순번을 받고 싶어요.", "timestamp": "2024-08-10T10:00:00Z"},
    {"conversation_id": "1", "sender": "ai_banker", "message": "안녕하세요! 어떤 업무를 보시려고 하나요?", "timestamp": "2024-08-10T10:00:05Z"}
]

# 임베딩 모델에서 반환된 384차원 벡터 사용 (임시로 랜덤 벡터 생성)
embeddings = [np.random.rand(embedding_size).tolist() for _ in data]

# 데이터 삽입
client.upsert(
    collection_name=collection_name,
    points=[
        {"id": i+1, "vector": embeddings[i], "payload": data[i]}
        for i in range(len(data))
    ]
)

print("초기 데이터가 성공적으로 삽입되었습니다.")
