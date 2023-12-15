import os

def create_directory(directory):
    # 자동으로 디렉터리를 생성하는 함수
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print(f"디렉터리를 만드는데 실패하였습니다 {directory}")