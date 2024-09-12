from flask import Flask, request, jsonify
import numpy as np
from numba import cuda

app = Flask(__name__)

# CUDA 커널 함수: 두 벡터를 더함
@cuda.jit
def vector_add(a, b, c):
    idx = cuda.grid(1)  # 글로벌 인덱스 계산
    if idx < a.size:
        c[idx] = a[idx] + b[idx]

# GPU 연산 함수 (벡터 덧셈)
def gpu_inference():
    # 벡터 크기 설정 (데이터 크기 조정 가능)
    n = 1000000
    a = np.random.random(n).astype(np.float32)
    b = np.random.random(n).astype(np.float32)
    c = np.zeros(n, dtype=np.float32)

    # GPU 메모리로 복사
    a_device = cuda.to_device(a)
    b_device = cuda.to_device(b)
    c_device = cuda.device_array_like(c)

    # 블록과 그리드 크기 설정
    threads_per_block = 256
    blocks_per_grid = (a.size + threads_per_block - 1) // threads_per_block

    # CUDA 커널 호출
    vector_add[blocks_per_grid, threads_per_block](a_device, b_device, c_device)

    # 결과를 CPU 메모리로 복사
    c_device.copy_to_host(c)

    # 결과 확인
    return c[:5]  # 결과의 처음 5개 값을 반환

# API 엔드포인트: GPU 연산 수행
@app.route('/generate', methods=['POST'])
def generate():
    # 입력 데이터에서 벡터 크기 받기 (기본 값: 1000000)
    data = request.json
    n = data.get('vector_size', 1000000)

    # 벡터 크기 제한 (메모리 초과 방지)
    if n > 1000000:
        return jsonify({'error': 'Vector size too large, max size is 1,000,000'}), 400

    # GPU 연산 수행
    try:
        result = gpu_inference()  # 결과로 벡터의 첫 5개 값 반환
        return jsonify({'result': result.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 헬스 체크 엔드포인트
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

# 앱 실행
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
