# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll.auto_reroll_image_init import *

stage_index = 4
stage_name = '中國'

def stage4(screen):

    battle_stage(screen, stage_index, stage_name, base_cat, wall_cat)
    
    # sleep(2)
    # wait_and_click(screen, btn_ok2)
    # sleep(2)
    # wait_and_click(screen, btn_ok2)

    # 獎勵
    # print('獎勵')
    while True:
        if screen.exists(btn_ok):
            screen.click(btn_ok)
            sleep(1)
        if screen.exists(btn_ok2):
            screen.click(btn_ok2)
            sleep(1)
        if screen.exists(fight_start):            
            break