import requests
import json
import datetime
import time
#import os
#from pprint import pprint

def KKboxCrawler(SongType, Area, Lang, Rank, Cate, Date):
    url = 'https://kma.kkbox.com/charts/api/v1/daily?category={}&date={}&lang={}&limit={}&terr={}&type={}'.format(Cate,Date,Lang,Rank,Area,SongType)
    res = requests.get(url)
    Orig_data = json.loads(res.text)
    Orig_data = Orig_data['data']['charts'][SongType]
    ReturnData=[]
    for i in range(int(Rank)):
        rerurn_data={}
        rk = Orig_data[i]['rankings']['this_period']
        rerurn_data['RK'] = rk                      #排名
        album = Orig_data[i]['album_name']
        rerurn_data['Album'] = album                #專輯
        artist = Orig_data[i]['artist_name']
        rerurn_data['Artist'] = artist              #歌手
        imgURL = Orig_data[i]['cover_image']['small']
        rerurn_data['ImgURL'] = imgURL              #縮圖
        song_id = Orig_data[i]['song_id']
        rerurn_data['SongID'] = song_id            #ID
        song_name = Orig_data[i]['song_name']
        rerurn_data['SongName'] = song_name        #歌名
        release_date = time.localtime(int(Orig_data[i]['release_date']))
        release_date = time.strftime("%Y-%m-%d", release_date)
        rerurn_data['ReleaseDate'] = release_date  #上架日期
        
        ReturnData.append(rerurn_data)
    return ReturnData
    
def CateType(Lang,Area):
    url = 'https://kma.kkbox.com/charts/api/v1/daily/categories?lang={}&terr={}&type=song'.format(Lang,Area)
    res = requests.get(url)
    data = json.loads(res.text)
    cate = [data['data'][i]['category_name'] for i in range(len(data['data']))]
    #print('cate:',cate)
    return cate

'''
#設定日期
Yday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
#print(Yday)
DBY = (datetime.date.today() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
#print(DBY)
'''


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

#print(KKboxCrawler('song','tw','tc','1','297',DBY))


#爬音樂曲風 CateType(Lang,Area)
#print(CateType('tc','tw'))




