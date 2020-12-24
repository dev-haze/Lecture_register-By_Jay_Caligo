#이름변경 : shift + f6




#셀레늄
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait


#bs4 & requests------------
from urllib.request import urlopen
from bs4 import BeautifulSoup

#import 끝
#=========================================================================
#코드 시작

#--------------------------봇 필터 우회용 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


#--------------------------
#URL = ''
testURL = 'https://www.google.com/webhp?hl=ko&ictx=2&sa=X&ved=0ahUKEwjJ0a-ug-btAhXHQN4KHafDB9YQPQgI'

driver = webdriver.Chrome(executable_path='chromedriver87.exe')
driver.get(url=testURL)




#--------------------------홈페이지 접속
html = urlopen(testURL)
bsobj = BeautifulSoup(html, 'html.parser')










print('hello')


