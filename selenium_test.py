from selenium import webdriver #1

#----------------봇 필터 우회용 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


#url = "https://www.google.com"#1
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"

#오류 시 chromedriver 경로 바꾸기 (c드라이브부터 .exe까지)#1
driver = webdriver.Chrome("C:/Users/bigla/OneDrive/문서/대학/수강신청서포터/Lecture_register-By_Jay_Caligo/chromedriver87.exe")#1
driver.get(url)#1

html = driver.page_source
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, features="html.parser")



import requests
session = requests.session()

params = dict()
params['m_id'] = 'biglai'
params['m_pw'] = 'dkdlwkr123!'

res = session.post(url, data=params)
res.raise_for_status()



#print(soup.span)

#print(soup.find_all('span', {'class': 'nickname MY_NICKNAME'}))

print(soup.find_all('span', ))



#print(res.headers)
#print(session.cookies.get_dict())





