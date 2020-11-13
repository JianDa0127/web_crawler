from KKboxCrawler import KKboxCrawler,YT_search,CateType
import datetime
from yt_download import Download

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

#設定日期
Yday = (datetime.date.today() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d')
#print(Yday)
DBY = (datetime.date.today() + datetime.timedelta(days=-2)).strftime('%Y-%m-%d')
#print(DBY)

#前天華語單曲日榜
# print(KKboxCrawler('song','tw','tc','2','297',DBY))

#昨天日語新歌日榜，取前5
# print(KKboxCrawler('newrelease','tw','tc','2','308',DBY))

#爬台灣地區有列入的音樂曲風 CateType(Lang,Area)
# print(CateType('tc','tw'))

#爬日本地區有列入的音樂曲風 CateType(Lang,Area)
# print(CateType('tc','jp'))

#爬華語單曲前幾名的yt搜尋連結
# yt URL = 'https://www.youtube.com/watch?v=' + 'ytID'
data = (KKboxCrawler('song','tw','tc','5','297',Yday))
data_songname = [data[i]['SongName'] for i in range(len(data))]
ytURL,ytURLfail = [],[]
rk=0
for Name in data_songname:
    rk+=1
    try:
        ytURL.append([str('%02d'%rk)+'_'+Name,YT_search(Name)])
    except:
        ytURLfail.append([rk,Name]) #因為延遲而沒抓到的網址
print('ytURL:',ytURL)
print('ytURL_fail:',ytURLfail)
# 下載目標檔案
for (name,ytid) in  ytURL:
    Download(name,ytid)




