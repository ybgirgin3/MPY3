# !/usr/bin/python3

# main issue
# progbar kısmında şarkı bittikten sonra tqdm kendini kapatmıyor
# bu da bir sonraki şarkıya geçmemizi engelliyor

import sys
import pafy
from random import choice
from pafVideo import pafier

def music_getter(details, playlist):
    x = choice(range(0, len(playlist)))
    id = details['items'][x]['pafy'].videoid
    link = 'https://www.youtube.com/watch?v='+id

    # print(link)
    pafier(link)
    music_getter(details, playlist)

def url_getter(url):
    # get url and make needed changes on it
    global details, playlist
    details = pafy.get_playlist(url)
    playlist = pafy.get_playlist2(url)

    print(details['title'])

    print('length of the playlist: {}'.format(len(playlist)))
    music_getter(details, playlist)
