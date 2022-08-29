# -*- coding:utf-8 -*-
from time import sleep
from sikulix4python import *
from auto_reroll.auto_reroll_image_init import *

from auto_reroll.stage1 import *
from auto_reroll.stage2 import *
from auto_reroll.stage3 import *
from auto_reroll.stage4 import *
from auto_reroll.stage5 import *
from auto_reroll.stage6 import *
from auto_reroll.stage7 import *

import pyautogui
import os
import shutil
import tkinter as tk
from tkinter import messagebox

if __name__ == '__main__':
    screen = Screen(1)

    while True:
        shutil.rmtree("C:/Program Files/Nox/bin/BignoxVMS/nox")
        shutil.copytree('C:/Program Files/Nox/bin/BignoxVMS/nox_bak', 'C:/Program Files/Nox/bin/BignoxVMS/nox')

        # 開啟nox
        screen.click(nox_icon)
        # 等待開啟
        sleep(20)
        screen.click(nox_zoom)

        # 開啟貓咪大戰爭
        # print('開啟遊戲')
        screen.click(battle_cat_app_icon)
        wait_for_img_exists(screen, btn_ok)
        screen.click(btn_ok)
        # ...等待資料下載
        # print('等待遊戲更新...')
        wait_for_img_exists(screen, game_foreword)
        # print('更新完成')
        screen.click(game_foreword)
        # print('前置動作')
        wait_for_img_exists(screen, game_contract_check)
        screen.click(game_contract_check)
        screen.click(game_contract_next)
        screen.click(game_contract_check)
        screen.click(game_contract_next)
        screen.click(btn_ok)
        screen.click(year)
        screen.click(num_2022)
        screen.click(month)
        screen.click(num_1)
        screen.click(day)
        screen.click(num_1)
        screen.click(how_old_ok)

        # 遊戲大廳
        # print('開始遊戲')
        screen.click(game_start)
        screen.click(fight_start)

        # stage 1
        stage1(screen)    

        # 每日獎勵
        # print('每日獎勵')
        while True:
            if screen.exists(btn_ok):
                screen.click(btn_ok)
                sleep(1)
            if screen.exists(btn_ok2):
                screen.click(btn_ok2)
                sleep(1)
            if screen.exists(code_ok):            
                screen.click(code_ok)
                break

        # 每日公告
        # print('每日公告')
        if screen.exists(announce_close):           
            screen.click(announce_close)
        # 禮包公告
        # print('禮包公告')
        if screen.exists(announce_back):           
            screen.click(announce_back)
        # 通關台灣公告
        # print('通關台灣公告')
        if screen.exists(small_close):           
            screen.click(small_close)
        # 禮包公告
        # print('新手禮包')
        if screen.exists(announce_back):           
            screen.click(announce_back)
        # 限時優惠
        # print('限時優惠')
        wait_and_click(screen, small_close)
        sleep(2)

        # 升級
        wait_and_click(screen, upgrade)
        sleep(2)
        img_upgrade_page_base_cat = screen.find(upgrade_page_base_cat)
        hover(img_upgrade_page_base_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        # 升級牆貓
        wait_and_click(screen, get_new_cat)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_back)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        wait_and_click(screen, btn_ok2)
        wait_and_click(screen, fight_start)

        # stage 2
        stage2(screen)    

        # 升級
        wait_and_click(screen, upgrade)
        sleep(2)
        # 升級貓
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_back)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        # stage 3
        stage3(screen)

        # 升級
        wait_and_click(screen, upgrade)
        sleep(2)
        img_upgrade_page_base_cat = screen.find(upgrade_page_base_cat)
        hover(img_upgrade_page_base_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        img_upgrade_page_wall_cat = screen.find(upgrade_page_wall_cat)
        hover(img_upgrade_page_wall_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        # 升級牆貓
        wait_and_click(screen, get_new_cat)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_back)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        # stage 4
        stage4(screen)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        # stage 5
        stage5(screen)

        # 開始戰鬥ㄦ
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        # stage 6
        stage6(screen)

        # 升級
        wait_and_click(screen, upgrade)
        sleep(2)
        img_upgrade_page_base_cat = screen.find(upgrade_page_base_cat)
        hover(img_upgrade_page_base_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        img_upgrade_page_wall_cat = screen.find(upgrade_page_wall_cat)
        hover(img_upgrade_page_wall_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        img_upgrade_page_warrior_cat = screen.find(upgrade_page_warrior_cat)
        hover(img_upgrade_page_warrior_cat.getCenter())
        pyautogui.drag(-200, 0, 0.5)
        # 升級牆貓
        wait_and_click(screen, get_new_cat)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_upgrade)
        wait_and_click(screen, btn_back)

        # 開始戰鬥
        wait_and_click(screen, fight_start)
        sleep(2)
        wait_and_click(screen, fight_start)

        # stage 7
        stage7(screen)

        wait_and_click(screen, get_cat_dex)
        wait_and_click(screen, get_activity)
        wait_and_click(screen, get_gashapon)
        wait_and_click(screen, get_level)
        wait_and_click(screen, get_cat_club)
        wait_and_click(screen, get_cat_stamp)

        while True:
            if screen.exists(btn_ok):
                screen.click(btn_ok)
                sleep(1)
            if screen.exists(btn_ok2):
                screen.click(btn_ok2)
                sleep(1)
            if screen.exists(announce_back):
                screen.click(announce_back)
                sleep(1)
            if screen.exists(announce_close):
                screen.click(announce_close)
                sleep(1)
            if screen.exists(small_close):
                screen.click(small_close)
                sleep(1)
                break
        
        wait_and_click(screen, rare_gashapon)
        wait_for_img_exists(screen, do_gashapon)

        get_super = False
        wait_and_click(screen, do_gashapon)
        wait_and_click(screen, btn_ok2)
        sleep(1)
        if screen.exists(get_super_rare_cat):
            get_super = True
        wait_and_click(screen, btn_ok2)
        wait_and_click(screen, do_gashapon)
        wait_and_click(screen, btn_ok2)
        sleep(1)
        if screen.exists(get_super_rare_cat):
            get_super = True
        wait_and_click(screen, btn_ok2)
        wait_and_click(screen, do_gashapon_with_can)
        wait_and_click(screen, yes)
        wait_and_click(screen, btn_ok2)
        sleep(1)
        if screen.exists(get_super_rare_cat):
            get_super = True
        wait_and_click(screen, btn_ok2)
        
        # print('finish')
        if get_super:
            root = tk.Tk()
            root.withdraw()
            result = messagebox.askquestion('抽到超激稀有！！！', '是否停止迴圈？')        
            if result == 'yes':
                exit()
        
        # print('關閉nox')
        screen.click(nox_close)
        sleep(10)