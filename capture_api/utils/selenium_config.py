import time
from datetime import datetime

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from capture_api.utils.common import create_directory


def elementExclude(driver,className=None,tagname=None, xpath=None):
    elements_to_exclude = []
    # 특정 요소를 제외하는 함수
    if className:
        elements_to_exclude = driver.find_elements(By.CLASS_NAME,className)
    elif tagname:
        elements_to_exclude = driver.find_elements(By.TAG_NAME, tagname)
    elif xpath:
        elements_to_exclude = driver.find_elements(By.XPATH, xpath)
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
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
    time.sleep(5)
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
    time.sleep(5)
    print(driver.current_url)
    print("로그인 성공")

def autoMbFaceBookLogin(driver, id, pw):
    # 자동으로 페이스북 로그인하는 함수
    driver.get("https://www.facebook.com/")
    wait = WebDriverWait(driver, 20)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "button")))
    time.sleep(5)
    username = driver.find_element(By.ID, "m_login_email")
    print("가져오기1")
    password = driver.find_element(By.ID, "m_login_password")
    print("가져오기2")
    # 파라미터로 전달받은 아이디와 패스워드 값
    username.send_keys(id)
    print("페이스북 아이디 입력")
    password.send_keys(pw)
    print("페이스북 비밀번호 입력")
    password.send_keys(Keys.ENTER)
    time.sleep(5)
    print(driver.current_url)
    print("로그인 성공")


def autoYouTubeLogin(id,pw):
    # 자동으로 유튜브 로그인하는 함수
    pass

def screenShot(filename, driver):
    # ec2
    # driver.save_screenshot(f"/home/ec2-user/{filename}.png")
    filepath = f"C://data/{filename}.png"
    driver.save_screenshot(filepath)
    now = datetime.now()
    # 날짜를 원하는 형식의 문자열로 변환
    formatted_date = now.strftime("%Y-%m-%d")
    return filepath
    # driver.save_screenshot(f"/home/appsvr/capture/test/{formatted_date}/{filename}.png")
    # print("스크린샷 저장 성공")
    # local
    # driver.save_screenshot(f"/Users/marmin/downloads/capture/{filename}.png")