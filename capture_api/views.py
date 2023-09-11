from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver

# Create your views here.
class ChromeService:
    pass


class ChromeDriverManager:
    pass


@api_view(['POST'])
def capture(request):
    '''
    Post 요청을 통해 이미지 크기, 너비, url, 파일 이름을 받아온 뒤
    셀레니움 라이브러리를 통해 캡쳐를 진행
    '''
    # 요청 데이터 파싱
    # path = "/Users/marmin/Downloads/chromedriver_mac_arm64/chromedriver"
    data = request.data
    url = data.get("urlPath",None)
    filename = data.get("filename", None)
    seq = 0
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome("/Users/marmin/Downloads/chromedriver_mac_arm64/chromedriver", options=chrome_options)
    driver = webdriver.Chrome( options=chrome_options)
    driver.get(url)
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width,height)
    # ec2
    driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
    # local
    # driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    driver.close()
    seq += 1

    return Response({'message':'캡쳐 성공'})