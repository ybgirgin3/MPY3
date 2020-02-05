import os
import sys
# import pygame
from random import choice
import colorama
from colorama import Fore, Back, Style
# import mutagen.mp3
import argparse # -> for cli 
import mimetypes # -> for controlling target file is media (audio) or not
from pydub import AudioSegment
from pydub.playback import play
from pprint import pprint

class Music:
    def __init__(self, music_dir, music_):
        # directory which includes musics
        self.music_dir = music_dir
        self.musics = []
        self.music_ = music_
        self.queue_ = ''
        self.mimestart = ''
        self.note_ = ['🎵','🎶','🎷','🎧','🎻', '🎺', '📻', '🎼', '']

    def music_finder(self, file_):
        # find music on file
        self.music_dir = os.listdir(file_)

        for music in self.music_dir:
            # initialize mimetype
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
            print('no music found :(')

        else:
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
            
            # we're going to make 
            self.music_ = os.path.join(path_, sngnm)
            tarS_ext = self.music_.split(os.extsep)
            s = AudioSegment.from_file(self.music_, tarS_ext[-1])

        else:
            self.music_ = os.path.join(path_, music2play_)
            sngnm = music2play_
            # print(self.musics) # ->  returns empty list

            # pydub needs file extension in it as a argument so get that for it
            tarS_ext = self.music_.split(os.extsep) # -> I used this style because 'os.path.splitext' returns file extension with dot in front of it pydub wants it without dot

            # extension is always last item of list
            s = AudioSegment.from_file(self.music_, tarS_ext[-1])

        # play song in the end
        print('\n\n\n')
        text = '......{0}...... Playing Song: {1}...........{0}.......'.format(choice(self.note_), sngnm)
        print(Fore.GREEN + text + Style.RESET_ALL)
        print('\n\n\n')
        try:
            play(s)
        except KeyboardInterrupt as e:
            print(Fore.RED + '\napp closed by user..')
            sys.exit(0)
    

    def main(self):
        # configure dir
        if args['song_name'] is None:
            if args['directory'] == 'pwd':
                args['directory'] = os.getcwd()

            self.music_finder(args['directory'])
            # print(type(self.music_finder(args['directory']))) # -> return list

        elif args['song_name'] is not None:
            self.music_player(args['directory'], args['song_name'])

# for argparsing
parser = argparse.ArgumentParser()
parser.add_argument('-dir', '--directory', help='Director path which full of tasty music, for current dir use "pwd" command')
parser.add_argument('-s', '--song_name', help='tasty song to listen -> for playing random song from dir use "all"')
args = vars(parser.parse_args())


# need initializations
mimetypes.init()
colorama.init()

MusicApp = Music(args['directory'], args['song_name'])
MusicApp.main()
