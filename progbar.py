# !/usr/bin/env python3
# -*- coding: utf8 -*-
# author: Yusuf Berkay Girgin

import time
from tqdm import tqdm
from colorama import Fore
from sys import exit
# will send the lengh of the song as a second
def progbar(toolbar_width):
    for i in tqdm(range(toolbar_width), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
        # time.sleep(toolbar_width/100) # do real work here
        time.sleep(1)
    exit(0)
    
