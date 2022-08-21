# -*- coding:utf-8 -*-
import os
from time import sleep
from sikulix4python import *
import pyautogui
from all_cats import *

screen = Screen(1)

class CatnipBase():    
    def __init__(self, args):
        self.args = args

        self.img_lib_path            = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "img_lib")     # 圖庫
        
        self.img_stage_title         = os.path.join(self.img_lib_path, f'stage_title_{self.args.catnip_color}.PNG')        
        self.img_battle_start        = os.path.join(self.img_lib_path, 'battle_start.PNG')                # 戰鬥開始
        self.img_edit_team           = os.path.join(self.img_lib_path, 'edit_team.PNG')                   # 編輯隊伍
        self.img_use_last_team_ok    = os.path.join(self.img_lib_path, 'use_last_team_ok.PNG')            # 確認使用上次通關隊伍
        self.img_next_stage          = os.path.join(self.img_lib_path, 'next_stage.PNG')                  # 下一關按鈕
        self.img_bonus               = os.path.join(self.img_lib_path, 'bonus')                           # 獎勵
        self.img_find_dig_map        = os.path.join(self.img_lib_path, 'find_dig_map')                           # 獎勵
        self.img_energy_not_enough   = os.path.join(self.img_lib_path, 'energy_not_enough')               # 統帥力不足
        self.img_energy_reset_ok     = os.path.join(self.img_lib_path, 'energy_reset_ok')                 # 統帥力回復確定
        self.img_energy_reset_no     = os.path.join(self.img_lib_path, 'energy_reset_no')                 # 統帥力回復取消
        self.img_look_comershow_btn  = os.path.join(self.img_lib_path, 'look_comershow_btn')              # 看廣告
        self.img_finish_comershow_ok = os.path.join(self.img_lib_path, 'finish_comershow_ok')             # 看廣告完畢
        self.img_rainbow_catnip_exists = os.path.join(self.img_lib_path, 'rainbow_catnip_exists')             # 看廣告完畢
        self.img_worker_cat = os.path.join(self.img_lib_path, 'worker_cat')             # 看廣告完畢

        # 遊戲畫面螢幕index
        self.screen = Screen(1)

    # 等待圖片出現
    def wait_for_img_exists(self, screen, img):
        while not screen.exists(img):
            sleep(1)
    
    def use_cat(self, use_cats_method, use_cats):
        sleep(5)
        pyautogui.drag(250, 0, 0.5)

        while True:
            # 用貓方法
            use_cats_method(use_cats)

            if not self.screen.exists(self.img_worker_cat):
                print('stage clear')
                # 確認是否有獎勵
                if self.screen.exists(self.img_bonus):
                    self.screen.click(self.img_bonus)
                    sleep(2)
                    # 確認是否有發掘
                    if self.screen.exists(self.img_find_dig_map):
                        self.screen.click(self.img_find_dig_map)
                    # 確認是否有彩虹貓薄荷
                    if self.screen.exists(self.img_rainbow_catnip_exists):                        
                        # print('出現彩虹貓薄荷，請自己打，程式結束。')
                        # exit()
                        print('彩虹貓薄荷出現')
                        screen.click(self.img_energy_reset_ok)
                        self.use_cat(self.use_cats_method, { crazy_normal_cat, crazy_wall_cat, wall_cat, pole_cat, dance_cat })                        
                        break

                # 確定是否通關結束
                if self.screen.exists(self.img_next_stage):
                    # 按下一關
                    self.screen.click(self.img_next_stage)
                    # 等待轉回主畫面
                    self.wait_for_img_exists(self.screen, self.img_battle_start)
                    break
    
    # default
    def use_cats_method(self, use_cats):
        for cat in use_cats:
            try:
                if screen.exists(cat):
                    screen.click(cat)
            except Exception as ex:
                if ex is KeyboardInterrupt:
                    return
                pass

    def start(self, use_cats_method, use_cats):

        # 點一下螢幕2(cmd執行才能觸發)
        pyautogui.click(2400, 500)
        
        # 直接打關卡
        if self.args.stage_attack:
            self.use_cat(use_cats_method, use_cats)
            return

        # 確認是否進入關卡
        if self.args.catnip_color != 'green':
            if not self.screen.exists(self.img_stage_title):
                print (f'請進入 "進化的{self.args.catnip_color}貓薄荷" 關卡。')
                exit()

        # 編輯隊伍
        self.screen.click(self.img_edit_team)
        # 等待是否使用上次隊伍畫面出現
        self.wait_for_img_exists(self.screen, self.img_use_last_team_ok)
        self.screen.click(self.img_use_last_team_ok)

        # 當前已使用旗子數
        use_flag_count = 0

        sleep(2)

        # 持續通關
        while True:
            # 看廣告回體力
            if screen.exists(self.img_look_comershow_btn):
                screen.click(self.img_look_comershow_btn)
                screen.click(self.img_energy_reset_ok)
                sleep(45)
                screen.click(self.img_finish_comershow_ok)

            # 進關            
            self.wait_for_img_exists(screen, self.img_battle_start)
            self.screen.click(self.img_battle_start)
            print('進關')

            # 統帥力是否不足
            if self.screen.exists(self.img_energy_reset_ok):
                print('統率力不夠')
                if use_flag_count < self.args.use_flags:                
                    self.screen.click(self.img_energy_reset_ok)
                    use_flag_count += 1
                    print(f'使用棋子數{use_flag_count}')
                    # 進關                    
                    self.wait_for_img_exists(self.screen, self.img_battle_start)
                    self.screen.click(self.img_battle_start)
                    print('進關')
                    sleep(2)
                    # # 進關
                    # self.wait_for_img_exists(screen, self.img_battle_start)
                    # self.screen.click(self.img_battle_start)
                else:
                    self.screen.click(self.img_energy_reset_no)
                    break

            # 打關卡
            self.use_cat(use_cats_method, use_cats)
            
            # 打完一次就結束
            if not self.args.run_out_energy:
                break