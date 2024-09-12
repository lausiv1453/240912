import os
import subprocess

# 폴더 경로 설정
hand_package_dir = "hand-packages"
package_dir = "packages"

# 수동 설치 패키지 다운로드 및 설치 함수
def install_manual_packages():
    if not os.path.exists(hand_package_dir):
        os.makedirs(hand_package_dir)

    # Python 3.9 및 필수 패키지 다운로드
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "python39"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "python39-pip"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "python39-devel"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "gcc"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "git"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "curl"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "make"], shell=True)

    # Docker-Compose 설치
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "docker-compose"], shell=True)

    # Qdrant 설치 (수동 설치용 다운로드)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "qdrant-client"], shell=True)

    # Setuptools (distutils 설치용)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "setuptools"], shell=True)

    # CUDA 관련 패키지 설치 (필요한 경우)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "numba"], shell=True)
    subprocess.run(["pip", "download", "--dest", hand_package_dir, "numpy"], shell=True)

# 자동 패키지 설치 함수
def download_packages(requirements_file):
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)

    with open(requirements_file, "r") as f:
        packages = f.readlines()

    for package in packages:
        package = package.strip()
        if package:
            print(f"Downloading {package}...")
            subprocess.run([f"pip download --no-deps --dest {package_dir} {package}"], shell=True)

# 각 모듈별 requirements.txt 경로
requirements_files = [
    "llm/requirements.txt",
    "embedding_model/requirements.txt",
    "framework/requirements.txt",
    "vector_db/requirements.txt"
]

# 수동 설치 수행
install_manual_packages()

# 자동 패키지 설치 수행
for req_file in requirements_files:
    download_packages(req_file)

print("All packages have been downloaded and saved to the respective folders.")
