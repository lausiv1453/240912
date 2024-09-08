from flask import Flask, jsonify

app = Flask(__name__)

# 기본 경로 설정
@app.route('/')
def index():
    return "Welcome to the Framework API", 200

# 기존의 RAG Pipeline을 위한 경로 예시
@app.route('/query', methods=['POST'])
def query():
    data = request.json
    message = data['message']
    
    # embed 요청
    embed_response = requests.post('http://embedding_model:8000/embed', json={'text': message})
    embedding = embed_response.json()['embedding']
    
    # vector DB 검색
    search_response = requests.post('http://vector_db:8001/search', json={'vector': embedding})
    search_result = search_response.json()
    
    if search_result:
        similar_message = search_result[0]['payload']['message']
        response = f"Found similar message: {similar_message}"
    else:
        response = "No related answers found."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
