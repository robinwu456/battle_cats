# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

if __name__ == '__main__':

    cat_img_path = 'C:/Users/RB/source/repos/the_battle_cats/img_lib/normal_cat_enabled.PNG'

    while (True):
        screen = Screen(1)
        if screen.exists(cat_img_path):
            screen.click(cat_img_path)
        sleep(1)
