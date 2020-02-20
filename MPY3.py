# !/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Yusuf Berkay Girgin
# date: 8 Feb 2020
import os
import sys
import vlc
import pafy
import argparse
import colorama
import mimetypes
from random import choice
from pprint import pprint
from mutagen.mp3 import MP3
from pydub import AudioSegment
from pydub.playback import play
from colorama import Fore, Style
from pydub.utils import mediainfo

class Music:
    def __init__(self, music_dir, music_):
        # directory which includes musics
        self.music_dir = music_dir
        self.musics = []
        self.music_ = music_
        self.mimestart = ''
        self.note_ = ['🎵','🎶','🎷','🎧','🎻', '🎺', '📻', '🎼', '']


    def music_finder(self, file_):
        # find music on file
        if file_ is None:
            print(Fore.RED+ 'You need to give "--dir" argument at least')
            sys.exit(0)
        self.music_dir = os.listdir(file_)

        for music in self.music_dir:
            # get mimetype of the files in the folder
            # we need it for grapping audio and video files from folder
            self.mimestart = mimetypes.guess_type(music)[0]
            if self.mimestart != None:
                self.mimestart = self.mimestart.split('/')[0]
                # if turning value is audio or video grap 'em
                if self.mimestart in ('audio', 'video'):
                    # return them as a list
                    self.musics.append(music)

        if len(self.musics) == 0:
            print(Fore.YELLOW + 'no music found :(')

        else:
            print(Fore.GREEN+ '*'*100)
            print(Style.RESET_ALL)
            pprint(self.musics)
        # return names of song in target dir as a list
        return self.musics

    

    def music_player(self, path_, music2play_):

        # if --song_name gets 'all' argument
        if music2play_ == 'all':
            # music_finder function will return song names as a list

            # msc is path of the target directory
            msc = self.music_finder(path_)
            # sngnm is one the song which python chose from target folder
            sngnm = choice(msc)
            
            # we're going to make join songs path and song's name
            self.music_ = os.path.join(path_, sngnm)

            tarS_ext = self.music_.split(os.extsep)
            # playable song
            s = AudioSegment.from_file(self.music_, tarS_ext[-1])

        else:
            # the song script need to play specified song
            self.music_ = os.path.join(path_, music2play_)

            msc = self.music_finder(path_)

            # sngnm is music name which is not 'all'
            sngnm = music2play_

            # print(self.musics) # ->  returns empty list

            # pydub needs file extension in it as a argument so get that for it
            # tarS_ext aka target song extension
            tarS_ext = self.music_.split(os.extsep) # -> I used this style because 
            # 'os.path.splitext' returns file extension with dot in front of it pydub wants it without dot

            # extension is always last item of list
            s = AudioSegment.from_file(self.music_, tarS_ext[-1])


        # play song in the end
        print('\n\n\n')
        text = '......{0}...... Playing Song: {1} ...........{0}.......'.format(choice(self.note_), sngnm)
        print(Fore.GREEN + text + Style.RESET_ALL)
        print('\n\n\n')
        try:
            # seçilen şarkıyı çal

            # aynı anda ikisini birden yapmıyor
            # from progbar import progbar
            # progbar(int(float(mediainfo(self.music_)['duration'])))
            play(s)
            # for auto-shuffle run musicplayer function again with 'all' argument
            self.music_player(path_, music2play_ = 'all')


        except KeyboardInterrupt as e:
            print(Fore.RED + '\napp closed by user..')
            sys.exit(0)
    

    def singlefromYT(self, url):
        from pafVideo import pafier
        pafier(url, choice(self.note_))

        
    def playlistFromYT(self, url):
        import playlist_
        playlist_.url_getter(url)




    def main(self):
        # dir var mı yok mu

        # dir varken
        # dir varken zaten direk olarak local müziklerden çalmaya çalışılıyor demek 
        # o yüzden youtube işine girmeye gerek yok burda
        
        if args['directory'] is not None:
            # eğer song varsa
            if args['song_name'] is not None:
                self.music_player(args['directory'], args['song_name'])

            # eğer song yoksa
            elif args['song_name'] is None:
                # direk olarak dir adı ile muzik ara
                # ararken eğer dir adı 'pwd' ise 
                if args['directory'] == 'pwd':
                    args['directory'] = os.getcwd()
                # daha sonra bunu direk olarak music_finder'in içinde yolla
                self.music_finder(args['directory'])

        # eper dir yoksa
        elif args['directory'] is None:
            # song name yoksa
            if args['song_name'] is None:
                # youtube için kontrol et

                # eğer youtube varsa
                if args['youtube'] is not None:
                    # NOTE:
                    # iki tane parsing değerini
                    # argümen eklemeden kullanamıyoruz
                    # o yüzden ya youtube için saçma bir varsayılan argüman değeri tanımlayacağız ya da 
                    # youtube yokken playlist argümanını alacağız
                    if args['playlist'] is None:
                        self.singlefromYT(args['youtube'])

                elif args['youtube'] is None:
                    if args['playlist'] is not None:
                        self.playlistFromYT(args['playlist'])



    """
    def main(self):
        # configure dir
        if args['song_name'] is None:

            if args['directory'] is None:
                if args['youtube'] is None:
                    if args['playlist'] is not None:
                        self.playlistFromYT(args['playlist'])


                elif args['youtube'] is not None:
                    # to pafy func
                    self.fromYT(args['youtube'])
               
            if args['directory'] == 'pwd':
                args['directory'] = os.getcwd()

            self.music_finder(args['directory'])
            # print(type(self.music_finder(args['directory']))) # -> return list

        elif args['song_name'] is not None:
            self.music_player(args['directory'], args['song_name'])
        """


# for argparsing
parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory', help='Director path which full of tasty music, for current dir use "pwd" command')
parser.add_argument('-s', '--song_name', help='tasty song to listen -> for playing random song from dir use "all"')
parser.add_argument('-y', '--youtube', help='listen song from youtube instead of local one')
parser.add_argument('-p', '--playlist', help='process on a playlist from youtube.. sadly it only supports shuffle mode and requires tp re-run every single time to get different song for now.. :(')
args = vars(parser.parse_args())


# need initializations
mimetypes.init()
colorama.init()

MusicApp = Music(args['directory'], args['song_name'])
MusicApp.main()

