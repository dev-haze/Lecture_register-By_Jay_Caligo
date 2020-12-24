from selenium import webdriver #1


url = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com" # 로그인페이지 url 넣기

#========================================================================================================================================================================
def login():
    #아이디 & 비번
    id = "biglai"
    pw = "dkdlwkr123!"

    id_box = driver.find_element_by_xpath("//*[@id='id']") #로그인 아이디 입력 박스 검사해서 따온 xpath 넣기
    id_box.click()
    id_box.clear()
    id_box.send_keys(id)

    pw_box = driver.find_element_by_xpath("//*[@id='pw']") #로그인 비번 입력 박스 검사해서 따온 xpath 넣기
    pw_box.click()
    pw_box.clear()
    pw_box.send_keys(pw)

    submit = driver.find_element_by_xpath("//*[@id='log.login']")  # 로그인 비번 입력 박스 검사해서 따온 xpath 넣기
    submit.click()


    


#========================================================================================================================================================================




#----------------봇 필터 우회용 코드
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}




#오류 시 chromedriver 경로 바꾸기 (c드라이브부터 .exe까지)#1
driver = webdriver.Chrome("C:/Users/bigla/OneDrive/문서/대학/수강신청서포터/Lecture_register-By_Jay_Caligo/chromedriver87.exe")#1
driver.get(url)#1


login() #####------------------------------





while(1):
    a = 1

#pw_box = driver.find_element_by_xpath("//*[@id='pw']")
#pw_box.click()
