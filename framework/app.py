from flask import Flask, request, jsonify, render_template
from qdrant_client import QdrantClient
import requests

app = Flask(__name__)

# Qdrant 클라이언트 설정
client = QdrantClient(host='vector_db', port=6333)

# index 페이지 경로 추가
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    message = data['message']
    
    # Step 1: Embed 요청
    try:
        embed_response = requests.post('http://embedding_model:8000/embed', json={'text': message})
        embedding = embed_response.json().get('embedding')

        # 임베딩 벡터 크기 확인 (예외처리하지 않고 출력만 진행)
        if not isinstance(embedding, list):
            print("임베딩 벡터가 리스트 형식이 아닙니다.")
        elif len(embedding) != 384:
            print(f"임베딩 벡터 크기: {len(embedding)} (384차원이 아닙니다.)")

    except Exception as e:
        return jsonify({'response': 'Embedding 모델 요청 실패: ' + str(e)})

    # Step 2: Vector DB 검색
    try:
        search_result = client.search(
            collection_name="my_collection",
            query_vector=embedding,
            limit=1,
            with_payload=True  # 페이로드 포함
        )
    except Exception as e:
        return jsonify({'response': 'Vector DB 검색 실패: ' + str(e)})

    # 검색 결과 처리
    if search_result:
        first_match = search_result[0]  # 첫 번째 검색 결과 객체 가져오기
        similar_message = first_match.payload['message']  # payload 속성으로 접근
        response = f"유사한 메시지: {similar_message}"
    else:
        response = "관련된 답변을 찾을 수 없습니다."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
