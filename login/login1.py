from selenium import webdriver
import time

# 1========================================================================================================================================================================
# ----------------봇 필터 우회용 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# 사람처럼 보이게 하는 옵션들
options = webdriver.ChromeOptions()
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정
# ========================================================================================================================================================================





url = "http://sugang.pcu.ac.kr/common/login.do?method=login"  # 로그인페이지 url 넣기
id = '2061025'
pw = 'DKDLWKR123!'


driver = webdriver.Chrome("C:/Users/bigla/OneDrive/문서/대학/수강신청서포터/Lecture_register-By_Jay_Caligo/chromedriver87.exe")#1
driver.get(url)
#id
driver.execute_script("document/getElementsByName('id')[0].value=\'"+id+"\'")
#pw
driver.execute_script("document/getElementsByName('id')[0].value=\'"+id+"\'")














