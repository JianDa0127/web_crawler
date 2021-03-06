from urllib.request import urlretrieve
from selenium import webdriver
import time
import os

def get_audio(SongType, Area, Lang, Rank, Cate, Date):
    #背景執行
    # url = 'https://kma.kkbox.com/charts/daily/{}?cate={}&date={}&lang={}&terr={}'.format(SongType,Cate,Date,Lang,Area)
    # options = webdriver.ChromeOptions() 
    # options.add_argument('--headless')    
    # browser = webdriver.Chrome(chrome_options=options, executable_path="./chromedriver.exe") # 背景執行
    # browser.get(url)
    
    url = 'https://kma.kkbox.com/charts/daily/{}?cate={}&date={}&lang={}&terr={}'.format(SongType,Cate,Date,Lang,Area)
    browser = webdriver.Chrome() 
    browser.get(url)
    
    #建立資料夾存放試聽檔
    AudioPath = "audio"
    if not os.path.isdir(AudioPath): #檢查資料夾是否存在
        os.mkdir(AudioPath)
    #建立資料夾存放歌詞
    lyricsPath = "lyrics"
    if not os.path.isdir(lyricsPath): #檢查資料夾是否存在
        os.mkdir(lyricsPath)
   

    Rank = int(Rank)+1 if int(Rank)>30 else int(Rank)
    for i in range(2,Rank+2):
        if i == 32: continue #跳過例外
        #單曲頁面
        browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[{}]/a/div/div[1]/span[1]/span[1]".format(i)).click()
        browser.implicitly_wait(5)
       
        
        #試聽檔案
        browser.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/button[1]").click()
        browser.implicitly_wait(5)
        audio = browser.find_element_by_tag_name('audio') #試聽檔案位置
        
        #儲存試聽檔案
        song_name = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/h1').text
        song_name = song_name.split(' -')[0].split(' (')[0].replace('?','')
        artist_name =browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div[1]/div/dl/dd/a').text
    
        try:
            urlretrieve(audio.get_attribute('src'), os.path.join(AudioPath, "30s-{}-{}.mp3".format(song_name, artist_name)))
            # urlretrieve(audio.get_attribute('src'),"30s_{:02d}-{}.mp3".format(i-2 if i>32 else i-1,song_name))
            time.sleep(1) #確保下載完整
            # print('[Success 30s download]',song_name)
        except:
            print('[Fail 30s download]',song_name)
            pass
            
        #儲存歌詞檔案
        try:
            lyrics = browser.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[1]/p').text
            f = open( lyricsPath + "\\" +'{}-{}.txt'.format(song_name,artist_name), 'w',encoding="utf-8")
            f.write(lyrics)
            f.close()
        except:
            print('[Fail download]',song_name)
            pass
        
        browser.back() #上一頁
    #關瀏覽器
    browser.close()


# 測試 get_audio(SongType, Area, Lang, Rank, Cate, Date)
get_audio('song','tw','tc','50','104','2020-11-15')
