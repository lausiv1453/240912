# RHEL 8.6 기반 이미지 사용
FROM registry.access.redhat.com/ubi8/ubi:8.6

# 작업 디렉토리 설정
WORKDIR /app

# 로컬 설치 패키지 복사 및 설치
COPY hand-packages /app/hand-packages
RUN rpm -i /app/hand-packages/python39*.rpm && \
    rpm -i /app/hand-packages/gcc*.rpm && \
    rpm -i /app/hand-packages/git*.rpm && \
    rpm -i /app/hand-packages/curl*.rpm && \
    rpm -i /app/hand-packages/make*.rpm

# Python3 기본 설정
RUN alternatives --set python /usr/bin/python3.9

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt --find-links /app/hand-packages

# 애플리케이션 파일 복사
COPY . .

# 애플리케이션 실행
CMD ["python3", "app.py"]
