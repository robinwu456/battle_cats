# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll_image_init import *

def stage1(screen):
    print('1/7')
    # print('第1關 - 台灣')
    wait_for_img_exists(screen, stage_1_teach_title)
    sleep(1)
    screen.click(stage_1_teach_title)
    # print('一堆提示')
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)
    wait_for_img_exists(screen, base_cat)
    screen.click(base_cat)
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)
    wait_for_img_exists(screen, btn_ok)
    screen.click(btn_ok)

    # print('出貓咪')
    while True:
        if screen.exists(base_cat):
            screen.click(base_cat)
        if screen.exists(btn_ok):
            screen.click(btn_ok)
        if screen.exists(win):
            # print('第一關結束')
            sleep(2)
            screen.click(win)
            screen.click(stage_complete_ok)
            break    
    wait_for_img_exists(screen, treasure_info)
    screen.click(treasure_info)
    screen.click(store_info)
    screen.click(mission_info)     