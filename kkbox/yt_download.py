from pytube import YouTube
from moviepy.editor import VideoFileClip
# import time

def Download(SongName,ytID):
    # t1 = time.time()
    url = YouTube('https://www.youtube.com/watch?v={}'.format(ytID))
    file=url.streams.filter().first()
    # print(file)
    file.download(filename=SongName)
    video = VideoFileClip('{}.mp4'.format(SongName))
    video.audio.write_audiofile('{}.mp3'.format(SongName))
    # t3 = time.time()
    
    # print('{}、{}'.format(t2-t1,t3-t2))
    
# Download('地球上最浪漫的一首歌','bCB_nIdN86s')