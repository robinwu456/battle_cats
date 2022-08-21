# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *

import pyautogui
from auto_reroll_image_init import *

stage_index = 2
stage_name = '香港'

def stage2(screen):

    battle_stage(screen, stage_index, stage_name, base_cat, wall_cat)