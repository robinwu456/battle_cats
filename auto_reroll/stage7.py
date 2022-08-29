# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll.auto_reroll_image_init import *

stage_index = 7
stage_name = '日本'

def stage7(screen):
    
    sleep(5)

    sleep(15)
    wait_and_click(screen, wall_cat)
    sleep(7)
    wait_and_click(screen, base_cat)
    sleep(7)
    wait_and_click(screen, base_cat)
    sleep(13)
    wait_and_click(screen, wall_cat)  

    sleep(6)    
    wait_and_click(screen, crazy_worker)
    # # print('錢包150')
    sleep(9)
    wait_and_click(screen, crazy_worker)
    # print('錢包200')
    sleep(15)
    wait_and_click(screen, crazy_worker)
    # print('錢包250')
    sleep(8)
    wait_and_click(screen, crazy_worker)
    # print('錢包300')

    sleep(13)
    wait_and_click(screen, wall_cat)  
    wait_and_click(screen, base_cat)

    sleep(10)
    wait_and_click(screen, wall_cat)
    sleep(4)  
    wait_and_click(screen, base_cat)

    sleep(11)
    wait_and_click(screen, crazy_worker)
    # print('錢包350')
    sleep(20)
    wait_and_click(screen, crazy_worker)
    # print('錢包400')

    sleep(7)
    wait_and_click(screen, wall_cat)  
    wait_and_click(screen, base_cat)

    sleep(25)
    wait_and_click(screen, leg_cat)

    result = battle_stage(screen, stage_index, stage_name, base_cat, wall_cat, warrior_cat)    

    # 戰敗
    if not result:
        wait_and_click(screen, small_close)
        wait_and_click(screen, no)
        wait_and_click(screen, btn_ok2)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        stage7(screen)