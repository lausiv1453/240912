from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
client = QdrantClient(host='vector_db', port=6333)
@app.route('/query', methods=['POST'])
def query():
    data = request.json
    message = data['message']
    
    # Embed the message
    embed_response = requests.post('http://embedding_model:8000/embed', json={'text': message})
    embedding = embed_response.json()['embedding']
    
    # Search the embedding in vector_db
    search_response = requests.post('http://vector_db:8001/search', json={'vector': embedding})
    search_result = search_response.json()
    
    # Generate response using llm
    if search_result:
        similar_message = search_result[0]['payload']['message']
        llm_response = requests.post('http://llm:8002/generate', json={'prompt': similar_message})
        response = llm_response.json()['response']
    else:
        response = "관련된 답변을 찾을 수 없습니다."
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
