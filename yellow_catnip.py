# -*- coding:utf-8 -*-
import sys
from time import sleep
from sikulix4python import *

img_lib_path            = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "img_lib")
img_stage_title         = os.path.join(img_lib_path, 'stage_title_angle.PNG')           # 神秘光芒 困難
img_battle_start        = os.path.join(img_lib_path, 'battle_start.PNG')          # 戰鬥開始
img_edit_team           = os.path.join(img_lib_path, 'edit_team.PNG')         # 編輯隊伍
img_use_last_team_ok    = os.path.join(img_lib_path, 'use_last_team_ok.PNG')          # 確認使用上次通關隊伍
img_next_stage          = os.path.join(img_lib_path, 'next_stage.PNG')          # 下一關按鈕
img_bonus               = os.path.join(img_lib_path, 'bonus')          # 獎勵
img_energy_not_enough   = os.path.join(img_lib_path, 'energy_not_enough')          # 統帥力不足
img_energy_reset_ok     = os.path.join(img_lib_path, 'energy_reset_ok')          # 統帥力回復確定

# use cat
img_noodle_cat       = os.path.join(img_lib_path, 'noodle_cat')       # 拉麵王
img_pole_cat         = os.path.join(img_lib_path, 'pole_cat')           # 撐竿跳貓
img_rockband_cat     = os.path.join(img_lib_path, 'rockband_cat')   # 搖滾樂團
img_bahamut_cat     = os.path.join(img_lib_path, 'bahamut_cat')   # 巴哈姆特貓

def wait_for_img_exists(screen, img):
    while not screen.exists(img):
        sleep(1)

if __name__ == '__main__':    
    screen = Screen(1)
    
    # 確認是否進入關卡
    if not screen.exists(img_stage_title):
        print ('請進入 "進化的黃色貓薄荷" 關卡。')
        exit()

    # 編輯隊伍
    screen.click(img_edit_team)
    # 等待是否使用上次隊伍畫面出現
    wait_for_img_exists(screen, img_use_last_team_ok)
    screen.click(img_use_last_team_ok)

    # 持續通關
    while True:
        # 進關
        wait_for_img_exists(screen, img_battle_start)
        screen.click(img_battle_start)

        # # 統帥力是否不足
        # if screen.exists(img_energy_not_enough):
        #     screen.click(img_energy_reset_ok)

        # 打關卡
        while True:
            # 出貓咪
            if screen.exists(img_noodle_cat):
                screen.click(img_noodle_cat)
            if screen.exists(img_pole_cat):
                screen.click(img_pole_cat)
            if screen.exists(img_rockband_cat):
                screen.click(img_rockband_cat)
            if screen.exists(img_bahamut_cat):
                screen.click(img_bahamut_cat)
            
            # 確認是否有獎勵
            if screen.exists(img_bonus):
                screen.click(img_bonus)

            # 確定是否通關結束
            if screen.exists(img_next_stage):
                # 按下一關
                screen.click(img_next_stage)
                # 等待轉回主畫面
                wait_for_img_exists(screen, img_battle_start)
                break