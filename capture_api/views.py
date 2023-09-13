from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    # 전송된 데이터 중 filename을 가져옴
    filename = data.get("filename", None)
    print("파싱 성공")
    # 파일 이름 중복 방지
    seq = 0
    # 크롬 옵션 설정하는 부분
    chrome_options = webdriver.ChromeOptions()
    print("옵션 불러오기 성공")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument('--lang=ko_KR.utf8')
    chrome_options.add_argument('--hide-scrollbars')
    print("옵션 설정 성공")
    # service = ChromeService(executable_path=ChromeDriverManager().install())
    # driver = webdriver.Chrome("/Users/marmin/Downloads/chromedriver_mac_arm64/chromedriver", options=chrome_options)
    # 옵션을 설정후 크롬 드라이버 호출
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    print("크롬 생성후 url 끌어오기 성공")
    a = url.split(".")
    # -----------------------FACEBOOK---------------------------------------
    if a[1] == "facebook":
        print("페이스북 입니다")
        # todo => 페이스북 관련 로직 작성/ 클래스값 확인 / 스크롤바 옵션 추가하기
    # -----------------------YOUTUBE---------------------------------------
    elif a[1] == "youtube":
        print("유튜브 입니다")
        # todo => 유뷰트 관련 로직 작성/ 클래스값 확인 / 스크롤바 옵션 추가하기
    # -----------------------INSTAGRAM---------------------------------------
    elif a[1] == "instagram":
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "x6s0dn4")))
        print("인스타그램 입니다")
        # todo => 인스타그램 관련 로직 작성/ 클래스값 확인/ 옵션 추가하기
        elementExclude(driver, "x1xgvd2v")
        elementExclude(driver, "_ab8q")
        elementExclude(driver,"_acbh")
        width = 1300
        height = 900
        driver.execute_script(f"window.innerWidth = {width};")
        driver.execute_script(f"window.innerHeight = {height};")
        driver.set_window_size(width, height)
        print("윈도우 사이즈 설정 성공")
        # 스크린샷 캡처
        # ec2
        # driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
        # print("스크린샷 저장 성공")
        # local
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    # -----------------------ETC---------------------------------------
    else:
        width = driver.execute_script("return document.body.scrollWidth")
        height = driver.execute_script("return document.body.scrollHeight")
        print('스크롤 설정 성공')
        driver.set_window_size(width, height)
        print("윈도우 사이즈 설정 성공")
        # ec2
        # driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
        # print("스크린샷 저장 성공")
        # local
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    driver.quit()
    seq += 1

    return Response({'message':'캡쳐 성공'})

# ------------------------유틸 함수------------------------------
def elementExclude(driver,className):
    # 특정 요소를 제외하는 함수
     elements_to_exclude = driver.find_elements(By.CLASS_NAME,className)
     # 찾은 요소를 숨기기 (CSS 스타일을 사용하여 숨기기)
     for element in elements_to_exclude:
         driver.execute_script("arguments[0].style.visibility = 'hidden';", element)