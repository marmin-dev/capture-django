import time

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# ------------------------유틸 함수------------------------------
def elementExclude(driver,className=None,tagname=None, xpath=None):
    # 특정 요소를 제외하는 함수
    if className:
        elements_to_exclude = driver.find_elements(By.CLASS_NAME,className)
    elif tagname:
        elements_to_exclude = driver.find_elements(By.TAG_NAME, tagname)
    elif xpath:
        elements_to_exclude = driver.find_elements(By.XPATH, xpath)
    print(elements_to_exclude)
    # 찾은 요소를 숨기기 (CSS 스타일을 사용하여 숨기기)
    for element in elements_to_exclude:
        driver.execute_script("arguments[0].style.visibility = 'hidden';", element)



def settingDriverSize(driver, width, height):
    # 드라이버 사이즈를 설정하는 함수
    driver.execute_script(f"window.innerWidth = {width};")
    driver.execute_script(f"window.innerHeight = {height};")
    driver.set_window_size(width, height)

def autoInstaLogin(id,pw):
    # 자동으로 인스타그램 로그인하는 함수
    pass
def autoFaceBookLogin(driver,id,pw):
    # 자동으로 페이스북 로그인하는 함수
    driver.get("https://www.facebook.com/")
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_42ft")))
    username = driver.find_element(By.ID, "email")
    print("가져오기1")
    password = driver.find_element(By.ID, "pass")
    print("가져오기2")
    # 파라미터로 전달받은 아이디와 패스워드 값
    username.send_keys(id)
    print("페이스북 아이디 입력")
    password.send_keys(pw)
    print("페이스북 비밀번호 입력")
    password.send_keys(Keys.ENTER)
    print("로그인 성공")


def autoYouTubeLogin(id,pw):
    # 자동으로 유튜브 로그인하는 함수
    pass

# -----------------Setting-------------------
# 크롬 옵션 설정하는 부분
# 크롬 드라이버 자동 실행되도록 (로그인 이슈/ 속도 이슈 해결)
chrome_options = webdriver.ChromeOptions()
print("옵션 불러오기 성공")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument('--lang=ko_KR.utf8')
chrome_options.add_argument('--hide-scrollbars')
print("옵션 설정 성공")
driver = webdriver.Chrome(options=chrome_options)
# ------- Login -------




# --------- 캡처 함수  --------

def capture(data):
    '''
    Post 요청을 통해 이미지 크기, 너비, url, 파일 이름을 받아온 뒤
    셀레니움 라이브러리를 통해 캡쳐를 진행
    '''
    # 요청 데이터 파싱
    # path = "/Users/marmin/Downloads/chromedriver_mac_arm64/chromedriver"

    url = data.get("urlPath",None)
    # 전송된 데이터 중 filename을 가져옴
    filename = data.get("filename", None)
    print("파싱 성공")
    # 파일 이름 중복 방지
    seq = 0
    driver.get(url)
    print("크롬 생성후 url 끌어오기 성공")
    a = url.split(".")
    # -----------------------FACEBOOK---------------------------------------
    if a[1] == "facebook":
        print("페이스북 입니다")
        if "photo/?fbid" in a[2]:
            # 이미지 창일 경우에 다른 랜딩페이지를 캡쳐하도록 하는 로직 작성
            print("캡쳐불가 => 랜딩 페이지로 리디렉트")
            hello = driver.find_element(By.XPATH,"//div//span//a")
            hello.click()
            print(driver.current_url)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
            time.sleep(2)
            # 캡쳐할 랜딩 페이지일 경우에 캡쳐하는 로직 작성
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        driver.implicitly_wait(3)
        # elementExclude(driver, "x1s65kcs")
        elementExclude(driver,xpath='//*[@role="navigation"]')
        width = 1600
        height = 850
        settingDriverSize(driver,width,height)
        # 스크린샷 캡처
        # ec2
        # driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
        # print("스크린샷 저장 성공")
        # local
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    # -----------------------YOUTUBE---------------------------------------
    elif a[1] == "youtube":
        print("유튜브 입니다")
        # todo => 유뷰트 관련 로직 작성/ 클래스값 확인 / 스크롤바 옵션 추가하기
        wait = WebDriverWait(driver, 10)
        element = EC.presence_of_all_elements_located((By.CLASS_NAME, "yt-img-shadow"))
        driver.implicitly_wait(4)
        width = 1600
        height = 850
        settingDriverSize(driver,width,height)
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        element = EC.presence_of_all_elements_located((By.CLASS_NAME, "yt-img-shadow"))
        time.sleep(4)
        # 스크린샷 캡처
        # ec2
        # driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
        # print("스크린샷 저장 성공")
        # local
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    # -----------------------INSTAGRAM---------------------------------------
    elif a[1] == "instagram":
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        driver.implicitly_wait(4)
        print("인스타그램 입니다")
        # todo => 인스타그램 관련 로직 작성/ 클래스값 확인/ 옵션 추가하기
        elementExclude(driver, "x1xgvd2v")
        elementExclude(driver, "_ab8q")
        elementExclude(driver,"_acbh")
        width = 1300
        height = 900
        settingDriverSize(driver,width, height)
        # 스크린샷 캡처
        # ec2
        # driver.save_screenshot(f"/home/ec2-user/{filename}{seq}.png")
        # print("스크린샷 저장 성공")
        # local
        driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}{seq}.png")
    # -----------------------ETC---------------------------------------
    else:
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        time.sleep(1)
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

    return '캡처 성공'

# ------------ api 함수 ------------

@api_view(['POST'])
def capture_one(request):
    data = request.data
    message = capture(data)
    return Response({"message": message})
@api_view(['POST'])
def capture_list(request):
    page_list = request.data
    for page in page_list:
        capture(page)
    return Response({"message":"캡쳐 성공"})


