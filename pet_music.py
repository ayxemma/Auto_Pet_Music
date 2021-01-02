#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 21:55:16 2018

@author: ayx
"""
import os
os.chdir(r'/usr/local/bin')
os.environ["PATH"] += os.pathsep + r"/usr/local/bin"

from selenium import webdriver

def music(menu):
    driver=webdriver.Chrome(executable_path=r"/usr/local/bin/chromedriver")
    musiclist=[
            "https://www.youtube.com/watch?v=2xttF0lM_Wk&start_radio=1&list=RDGMEMz3e4vKpJzevZUeQNb5kIlg", 
               "https://www.youtube.com/watch?v=UeS0VoMm8jY",
               "https://www.youtube.com/watch?v=xd9HC6bP42g",
               "https://www.youtube.com/watch?v=5L68ZdlbYDE",
               "https://www.youtube.com/watch?v=_gaJxJCr1ec",
               "https://www.youtube.com/watch?v=T7glYdBZV70",
               "https://www.youtube.com/watch?v=ctinmprZxLw",
               "https://www.youtube.com/watch?v=P9gFVzmAkpY",
               "https://www.youtube.com/watch?v=XqC05_Oommw",
               "https://www.youtube.com/watch?v=r1P9JAg3kXE"]
    
    driver.get(musiclist[menu])
    time.sleep(60*2)
    driver.quit()

if __name__ == "__main__":
    fname=r'~/menu.txt'
    if os.path.isfile(fname):
        with open(fname, 'r') as file:
            menu=int(file.read())
    else:
        menu=0
        
    with open(fname, 'w') as file:
        file.write(str(menu+1))
    
    music(menu)
    
