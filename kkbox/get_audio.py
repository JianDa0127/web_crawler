import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


def validateTitle(title): #替代特殊符號
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_title = re.sub(rstr, "_", title)  # 替換為下劃線
    return new_title


def get_audio(SongType, Area, Lang, Cate, Date):

    options = webdriver.ChromeOptions()  #背景執行
    options.add_argument('--headless')    

    browser = 'https://kma.kkbox.com/charts/daily/{}?cate={}&date={}&lang={}&terr={}'.format(SongType,Cate,Date,Lang,Area)
    # driver = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver.exe") # 背景執行
    driver = webdriver.Chrome(executable_path="./chromedriver.exe") 
    
    # driver.maximize_window() #全螢幕
    driver.get(browser)
    time.sleep(3)
    
        

    for i in range(2,53,1):
        if i == 32: #li[32] 出現例外
            continue
        driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[{}]/a/div/div[1]/span[1]/span[1]".format(i)).click()
        driver.implicitly_wait(5)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/button[1]").click()
        driver.implicitly_wait(5)
        
            
        audio=driver.find_element_by_tag_name('audio') #試聽檔案位置
        song_name=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/h1") #歌詞位置
        print(song_name.text) #下載歌詞 待補
        time.sleep(1)
        urllib.request.urlretrieve(audio.get_attribute('src'),"{}30S試聽.mp3".format(validateTitle(song_name.text)))
        time.sleep(1)
        print('done')
        driver.back()#上一頁
        


get_audio('song','tw','tc','104','2020-11-15')
