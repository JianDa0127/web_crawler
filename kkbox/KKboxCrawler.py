import requests
import json
# import datetime
import time
from selenium import webdriver
# import os
# from pprint import pprint

def YT_search(string):
    url = 'https://www.youtube.com/results?search_query={}'.format(string)
    
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    
    browser = webdriver.Chrome(chrome_options=option)
    browser.get(url)
    # time.sleep(1)
    xpath = browser.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a')
    href = xpath.get_attribute('href')
    # print(href,type(href))
    browser.close()
    
    return href.split('=')[1]

def KKboxCrawler(SongType, Area, Lang, Rank, Cate, Date):
    url = 'https://kma.kkbox.com/charts/api/v1/daily?category={}&date={}&lang={}&limit={}&terr={}&type={}'.format(Cate,Date,Lang,Rank,Area,SongType)
    res = requests.get(url)
    Orig_data = json.loads(res.text)
    Orig_data = Orig_data['data']['charts'][SongType]
    # print(Orig_data)
    ReturnData=[]
    for i in range(int(Rank)):
        rerurn_data={}
        #排名
        rk = Orig_data[i]['rankings']['this_period']
        rerurn_data['RK'] = rk                
        #歌名
        song_name = Orig_data[i]['song_name']
        song_name = song_name.split(' -')[0] #把歌名基本處理
        rerurn_data['SongName'] = song_name
        #歌手
        artist = Orig_data[i]['artist_name']
        rerurn_data['Artist'] = artist
        #專輯
        album = Orig_data[i]['album_name']
        rerurn_data['Album'] = album            
        #縮圖 'https://i.kfs.io/album/global/' + imgURL + ',0v1/fit/160x160.jpg'
        imgURL = Orig_data[i]['cover_image']['small']
        # imgURL = imgURL.split('global/')[1]
        # imgURL = imgURL.split(',')[0]
        rerurn_data['ImgURL'] = imgURL         
        #歌曲ID
        song_id = Orig_data[i]['song_id']
        rerurn_data['SongID'] = song_id      
        # yt網址 (因為常常跑太久當掉，所以沒放進)
        # yt URL = 'https://www.youtube.com/watch?v=' + 'ytID'
        # YT_vid = YT_search(song_name)
        # rerurn_data['ytID'] = YT_vid       
        #上架日期         
        release_date = time.localtime(int(Orig_data[i]['release_date']))
        release_date = time.strftime("%Y-%m-%d", release_date)
        rerurn_data['ReleaseDate'] = release_date  
        
        ReturnData.append(rerurn_data)
    return ReturnData
    
def CateType(Lang,Area):
    url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang={}&terr={}&type=song'.format(Lang,Area)
    res = requests.get(url)
    data = json.loads(res.text)
    cate = [data['data'][i]['category_name'] for i in range(len(data['data']))]
    # print('cate:',cate)
    return cate


#設定日期
# Yday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
# print(Yday)
# DBY = (datetime.date.today() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
# print(DBY)



#參數說明
# =============================================================================
# KKboxCrawler(SongType, Area, Lang, Rank, Cate, Date)
# SongType類型參數: 單曲song, 新歌newrelease
# Area地區參數：台灣tw、香港hk、日本jp、新加坡sg、馬來西亞my -->預設tw
# Lang語言參數: 本地tc、簡中sc、日文ja、英文en、馬來ms --> 預設tc
# Rank名次參數: 取前幾名 1~50
# Cate曲風參數: 華語297,西洋390,日語308,韓語314,台語304,粵語320,綜合104,馬來917,西方771,亞洲861
# Date日期參數: --> 昨天Yday、前天DBY、自訂YYYY-MM-DD
# =============================================================================

# print(KKboxCrawler('song','tw','tc','1','297',Yday))


#爬音樂曲風 CateType(Lang,Area)
# print(CateType('tc','tw'))




