from selenium import webdriver  # 1
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


import time

url = "http://sugang.pcu.ac.kr/common/login.do?method=login"  # 로그인페이지 url 넣기
# 아이디 & 비번
id = "2061025"
pw = "DKDLWKR123!"




# 1========================================================================================================================================================================
# ----------------봇 필터 우회용 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 사람처럼 보이게 하는 옵션들
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정
# ========================================================================================================================================================================





# 2========================================================================================================================================================================
# 오류 시 chromedriver 경로 바꾸기 (c드라이브부터 .exe까지)#1
driver = webdriver.Chrome("C:/Users/bigla/OneDrive/문서/대학/수강신청서포터/Lecture_register-By_Jay_Caligo/chromedriver87.exe",chrome_options=options)  # 1
driver.get(url)  # 1
#######################################################################################################




# 3<로그인>######################################################################################################
id_box = driver.find_element_by_xpath("//*[@id='memberNo']")  # 로그인 아이디 입력 박스 검사해서 따온 xpath 넣기
id_box.click()
id_box.clear()
id_box.send_keys(id)

time.sleep(1)

pw_box = driver.find_element_by_xpath("//*[@id='password']")  # 로그인 비번 입력 박스 검사해서 따온 xpath 넣기
pw_box.click()
pw_box.clear()
pw_box.send_keys(pw)

time.sleep(1)

#submit = driver.find_element_by_xpath("//*[@id='log']")  # 로그인 비번 입력 박스 검사해서 따온 xpath 넣기
#submit.click()

pw_box.send_keys(Keys.RETURN)

driver.implicitly_wait(1)
time.sleep(1)

WebDriverWait(driver, 10)
#######################################################################################################




#새로운 브라우저에서 로그인된 사이트 접속
#url = 'https://www.pcu.ac.kr/www/index/'
#driver.get(url)





# pw_box = driver.find_element_by_xpath("//*[@id='pw']")
# pw_box.click()




