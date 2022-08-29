# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll.auto_reroll_image_init import *

stage_index = 6
stage_name = '韓國'

def stage6(screen):
    
    battle_stage(screen, stage_index, stage_name, base_cat, wall_cat)
    
    wait_and_click(screen, get_new_cat_alarm)