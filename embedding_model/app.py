from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

# 300차원 벡터를 반환하는 모델로 변경
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

@app.route('/embed', methods=['POST'])
def embed():
    data = request.json
    text = data.get('text', '')
    
    # 임베딩 벡터 생성
    embedding = model.encode([text]).tolist()[0]
    
    # 벡터 크기 출력
    print(f"임베딩 벡터 크기: {len(embedding)}")
    
    return jsonify({'embedding': embedding})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
