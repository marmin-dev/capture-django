# --------- 캡처 함수  --------
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from capture_api.utils.selenium_config import elementExclude, settingDriverSize, screenShot, autoFaceBookLogin


def capture(data, driver):
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
    a = url.split(".")
    if a[1] != "facebook":
        driver.get(url)
        print("크롬 생성후 url 끌어오기 성공")
    # -----------------------FACEBOOK---------------------------------------
    if a[1] == "facebook":
        print("페이스북 입니다")
        # ------- Login -------
        autoFaceBookLogin(driver, "01095528693", "thpo4327")
        driver.get(url)
        print("크롬 생성후 url 끌어오기 성공")
        a = url.split(".")
        if "photo/?fbid" in a[2]:
            # 이미지 창일 경우에 다른 랜딩페이지를 캡쳐하도록 하는 로직 작성
            print("캡쳐불가 => 랜딩 페이지로 리디렉트")
            target_substring = "https://www.facebook.com/"

            # 모든 <a> 태그 찾기
            a_elements = driver.find_elements(By.XPATH,"//h2//span//span//a")

            # <a> 태그 반복 및 href 속성 확인 후 클릭
            for a_element in a_elements:
                href = a_element.get_attribute("href")  # href 속성 가져오기
                print(href)
                if href and target_substring in href:
                    a_element.click()
                    break  # 원하는 엘리먼트를 찾았으면 반복문 종료
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
        screenShot(filename, driver)
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
        screenShot(filename, driver)
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        element = EC.presence_of_all_elements_located((By.CLASS_NAME, "yt-img-shadow"))
        time.sleep(4)
        # 스크린샷 캡처
        screenShot(filename, driver)
    # -------------------------- Instagram -------------------------------
    elif a[1] == "instagram":
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
        time.sleep(4)
        print("인스타그램 입니다")
        # todo => 인스타그램 관련 로직 작성/ 클래스값 확인/ 옵션 추가하기
        # elementExclude(driver, xpath= "//span//div//a")
        elementExclude(driver=driver,className="_acun")
        elementExclude(driver= driver,className="_ab8q")
        try:
            # X 버튼을 찾습니다.
            x_button = driver.find_element(By.CLASS_NAME, "_abn5")
            # X 버튼을 클릭합니다.
            x_button.click()
        except:
            # 엘리먼트를 찾지 못한 경우에 대한 예외 처리
            print("X 버튼을 찾을 수 없습니다.")
        # btn.click()
        # btn.send_keys(Keys.ENTER)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
        width = 1300
        height = 900
        settingDriverSize(driver,width, height)
        screenShot(filename,driver)
    # -----------------------ETC---------------------------------------
    else:
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        time.sleep(1)
        width = driver.execute_script("return document.body.scrollWidth")
        height = 2000
        print('스크롤 설정 성공')
        driver.set_window_size(width, height)
        print("윈도우 사이즈 설정 성공")
        screenShot(filename, driver)

    return '캡처 성공'

# ------------ api 함수 ------------
