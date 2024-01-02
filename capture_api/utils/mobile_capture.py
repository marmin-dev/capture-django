# --------- 캡처 함수  --------
import time
from io import BytesIO

from PIL import Image
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from capture_api.utils.selenium_config import elementExclude, settingDriverSize, screenShot, autoMbFaceBookLogin


def mobile_capture(data, driver):
    '''
    Post 요청을 통해 이미지 크기, 너비, url, 파일 이름을 받아온 뒤
    셀레니움 라이브러리를 통해 캡쳐를 진행
    '''
    # 요청 데이터 파싱
    # path = "/Users/marmin/Downloads/chromedriver_mac_arm64/chromedriver"
    return_message = []
    url = data.get("urlPath",None)
    # # 전송된 데이터 중 filename을 가져옴
    filename = data.get("filename", None)
    print("파싱 성공")
    # # 파일 이름 중복 방지
    a = url.split(".")
    print(a)
    # -----------------------FACEBOOK---------------------------------------
    if a[1] == "facebook":
        print("페이스북 입니다")
        width = 600
        height = 850
        settingDriverSize(driver, width, height)
        # ------- Login -------
        autoMbFaceBookLogin(driver, "01095528693", "thpo4327")
        driver.get(url)
        print("크롬 생성후 url 끌어오기 성공")
        a = url.split(".")
        if "photo/?fbid" in a[2]:
            # 이미지 창일 경우에 다른 랜딩페이지를 캡쳐하도록 하는 로직 작성
            print("캡쳐불가 => 랜딩 페이지로 리디렉트")
            target_substring = "https://www.facebook.com/"
            # 모든 <a> 태그 찾기
            x_elements = driver.find_elements(By.XPATH, "//div/div/button")
            for x in x_elements:
                data_action_id = x.get_attribute("data-action-id")
                if data_action_id == 16:
                    x.click()
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

        return_message = screenShot(filename, driver, url)
    # -----------------------YOUTUBE---------------------------------------
    elif a[1] == "youtube":
        print("유튜브 입니다")
        driver.get(url)
    #     # todo => 유뷰트 관련 로직 작성/ 클래스값 확인 / 스크롤바 옵션 추가하기
        wait = WebDriverWait(driver, 10)
        element = EC.presence_of_all_elements_located((By.CLASS_NAME, "yt-img-shadow"))
        driver.implicitly_wait(4)
        width = 500
        height = 850
        settingDriverSize(driver,width,height)
        screenShot(filename, driver,url)
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        element = EC.presence_of_all_elements_located((By.CLASS_NAME, "yt-img-shadow"))
        time.sleep(4)
        # 스크린샷 캡처
        return_message = screenShot(filename, driver, url)
    # -------------------------- Instagram -------------------------------
    elif a[1] == "instagram":
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
        time.sleep(4)
        print("인스타그램 입니다")
    #     # todo => 인스타그램 관련 로직 작성/ 클래스값 확인/ 옵션 추가하기
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

        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "canvas")))
        width = 500
        height = 1100
        settingDriverSize(driver,width, height)
        return_message = screenShot(filename,driver,url)
        with open(return_message[2], 'rb') as f:
            image = Image.open(BytesIO(f.read()))
        cropped = image.crop((0,0,500,700))
        cropped.save(return_message[2])
    # -----------------------ETC---------------------------------------

    else:
        driver.get(url)
        wait = WebDriverWait(driver, 20)
        element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "img")))
        time.sleep(1)
        width = 500
        height = 880
        print('스크롤 설정 성공')
        driver.set_window_size(width, height)
        print("윈도우 사이즈 설정 성공")
        return_message = screenShot(filename, driver,url)
        print(return_message)
    return return_message

# ------------ api 함수 ------------
