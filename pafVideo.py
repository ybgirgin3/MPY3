# !/usr/bin/env python3
import pafy
import vlc
import colorama
from progbar import progbar

# pafy side

# kavinsky nighcall
# url = 'https://www.youtube.com/watch?v=MV_3Dpw-BRY&list=RDMV_3Dpw-BRY&start_radio=1'

# rammstein mein land
# url = 'https://www.youtube.com/watch?v=6iaxDxHUWP8&list=RDMV_3Dpw-BRY&index=3&has_verified=1'

# slipknot unsainted
# url = 'https://www.youtube.com/watch?v=VpATBBRajP8'
colorama.init()

def pafier(url, icon):
    video = pafy.new(url)
    best = video.getbestaudio()
    # media = vlc.MediaPlayer("/home/berkay/Müzik/Kavinsky__Nightcall_Drive_Original_Movie_Soundtrack.mp4")
    media = vlc.MediaPlayer(best.url)
    text = '.....{1}....{0} playing from youtube...{1}...'.format((video.title), icon)
    print(colorama.Fore.GREEN + text + colorama.Style.RESET_ALL)

    media.play()
    # return video.length
    progbar(video.length)
    while True:
        pass

# end file
