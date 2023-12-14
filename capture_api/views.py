from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver


from capture_api.utils.capture import capture

chrome_options = webdriver.ChromeOptions()
print("옵션 불러오기 성공")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--lang=ko_KR.utf8')
chrome_options.add_argument('--hide-scrollbars')
print("옵션 설정 성공")
print("캡쳐 프로그램 실행")

@api_view(['POST'])
def capture_one(request):
    driver = webdriver.Chrome(options=chrome_options)
    # 디버깅을 위한 드라이버 로깅 활성화
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--log-level=0")

    data = request.data
    message = capture(data, driver)
    return Response({"message": message})

@api_view(['POST'])
def capture_list(request):

    driver = webdriver.Chrome(options=chrome_options)
    # 디버깅을 위한 드라이버 로깅 활성화
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--log-level=0")

    page_list = request.data
    for page in page_list:
        capture(page, driver)
    return Response({"message":"캡쳐 성공"})

@api_view(['POST'])
def mobile_capture_one(request):
    user_agt = 'Mozilla/5.0 (Linux; Android 9; INE-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agt}')
    driver = webdriver.Chrome(options=chrome_options)
    # 디버깅을 위한 드라이버 로깅 활성화
    chrome_options.add_argument("--enable-logging")
    chrome_options.add_argument("--log-level=0")

    data = request.data
    message = capture(data, driver)
    return Response({"message": message})
