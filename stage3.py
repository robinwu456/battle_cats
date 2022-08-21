# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll_image_init import *

stage_index = 3
stage_name = '泰國'

def stage3(screen):

    battle_stage(screen, stage_index, stage_name, base_cat, wall_cat)
    
    wait_and_click(screen, get_new_cat_alarm)