from time import sleep
import os
from sikulix4python import *
import pyautogui

# 等待圖片出現
def wait_for_img_exists(screen, img):
    while not screen.exists(img):
        sleep(1)

# 等待並點擊
def wait_and_click(screen, img):
    wait_for_img_exists(screen, img)
    if img == fight_start or img == upgrade:
        i = screen.find(img)
        hover(i.getCenter())
        pyautogui.mouseDown()
        sleep(2)
        pyautogui.mouseUp()
    else:
        screen.click(img)

def battle_stage(screen, stage_index, stage_name, *args):
    # print(f'第{stage_index}關 - {stage_name}')        
    # print('出貓咪')
    print(f'{stage_index}/7')

    wait_for_img_exists(screen, base_cat)
    pyautogui.keyDown('-')
    sleep(2)
    pyautogui.keyUp('-')

    while True:
        is_cat_found = False
        for cat in args:
            try:
                if screen.exists(cat):
                    screen.click(cat)
                    is_cat_found = True
            except Exception as ex:
                if ex is KeyboardInterrupt:
                    return
                pass
        if not is_cat_found:
            if screen.exists(defeat):
                return False
        if screen.exists(win):
            # print(f'第{stage_index}關結束')
            sleep(2)
            screen.click(win)
            screen.click(stage_complete_ok)
            break    
    
    return True


img_lib_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "img_lib")     # 圖庫
auto_reroll_img_lib = os.path.join(img_lib_path, "auto_reroll")

nox_icon = os.path.join(auto_reroll_img_lib, 'nox_icon.PNG')
nox_close = os.path.join(auto_reroll_img_lib, 'nox_close.PNG')
nox_zoom = os.path.join(auto_reroll_img_lib, 'nox_zoom.PNG')
battle_cat_app_icon = os.path.join(auto_reroll_img_lib, 'battle_cat_app_icon.PNG')
app_info = os.path.join(auto_reroll_img_lib, 'app_info.PNG')
storage_space = os.path.join(auto_reroll_img_lib, 'storage_space.PNG')
clear_game_info = os.path.join(auto_reroll_img_lib, 'clear_game_info.PNG')
clear_game_info_confirm = os.path.join(auto_reroll_img_lib, 'clear_game_info_confirm.PNG')
home = os.path.join(auto_reroll_img_lib, 'home.PNG')
btn_ok = os.path.join(auto_reroll_img_lib, 'btn_ok.PNG')
btn_ok2 = os.path.join(auto_reroll_img_lib, 'btn_ok2.PNG')
btn_ok3 = os.path.join(auto_reroll_img_lib, 'btn_ok3.PNG')
stage_complete_ok = os.path.join(auto_reroll_img_lib, 'stage_complete_ok.PNG')
game_foreword = os.path.join(auto_reroll_img_lib, 'game_foreword.PNG')
game_contract_check = os.path.join(auto_reroll_img_lib, 'game_contract_check.PNG')
game_contract_next = os.path.join(auto_reroll_img_lib, 'game_contract_next.PNG')
year = os.path.join(auto_reroll_img_lib, 'year.PNG')
month = os.path.join(auto_reroll_img_lib, 'month.PNG')
day = os.path.join(auto_reroll_img_lib, 'day.PNG')
num_2022 = os.path.join(auto_reroll_img_lib, '2022.PNG')
num_1 = os.path.join(auto_reroll_img_lib, '1.PNG')
how_old_ok = os.path.join(auto_reroll_img_lib, 'how_old_ok.PNG')
game_start = os.path.join(auto_reroll_img_lib, 'game_start.PNG')
fight_start = os.path.join(auto_reroll_img_lib, 'fight_start.PNG')
stage_1_teach_title = os.path.join(auto_reroll_img_lib, 'stage_1_teach_title.PNG')
win = os.path.join(auto_reroll_img_lib, 'win.PNG')
treasure_info = os.path.join(auto_reroll_img_lib, 'treasure_info.PNG')
store_info = os.path.join(auto_reroll_img_lib, 'store_info.PNG')
mission_info = os.path.join(auto_reroll_img_lib, 'mission_info.PNG')
code_ok = os.path.join(auto_reroll_img_lib, 'code_ok.PNG')
announce_close = os.path.join(auto_reroll_img_lib, 'announce_close.PNG')
announce_back = os.path.join(auto_reroll_img_lib, 'announce_back.PNG')
small_close = os.path.join(auto_reroll_img_lib, 'small_close.PNG')
upgrade = os.path.join(auto_reroll_img_lib, 'upgrade.PNG')
upgrade_slidebar = os.path.join(auto_reroll_img_lib, 'upgrade_slidebar.PNG')
upgrade_page_base_cat = os.path.join(auto_reroll_img_lib, 'upgrade_page_base_cat.PNG')
upgrade_page_wall_cat = os.path.join(auto_reroll_img_lib, 'upgrade_page_wall_cat.PNG')
upgrade_page_warrior_cat = os.path.join(auto_reroll_img_lib, 'upgrade_page_warrior_cat.PNG')
get_new_cat = os.path.join(auto_reroll_img_lib, 'get_new_cat.PNG')
btn_upgrade = os.path.join(auto_reroll_img_lib, 'btn_upgrade.PNG')
btn_back = os.path.join(auto_reroll_img_lib, 'upgrade_back.PNG')
reach_mission = os.path.join(auto_reroll_img_lib, 'reach_mission.PNG')
get_new_cat_alarm = os.path.join(auto_reroll_img_lib, 'get_new_cat_alarm.PNG')
get_cat_dex = os.path.join(auto_reroll_img_lib, 'get_cat_dex.PNG')
get_activity = os.path.join(auto_reroll_img_lib, 'get_activity.PNG')
get_gashapon = os.path.join(auto_reroll_img_lib, 'get_gashapon.PNG')
get_level = os.path.join(auto_reroll_img_lib, 'get_level.PNG')
get_cat_club = os.path.join(auto_reroll_img_lib, 'get_cat_club.PNG')
get_cat_stamp = os.path.join(auto_reroll_img_lib, 'get_cat_stamp.PNG')
rare_gashapon = os.path.join(auto_reroll_img_lib, 'rare_gashapon.PNG')
do_gashapon = os.path.join(auto_reroll_img_lib, 'do_gashapon.PNG')
get_super_rare_cat = os.path.join(auto_reroll_img_lib, 'get_super_rare_cat.PNG')
do_gashapon_with_can = os.path.join(auto_reroll_img_lib, 'do_gashapon_with_can.PNG')
yes = os.path.join(auto_reroll_img_lib, 'yes.PNG')
no = os.path.join(auto_reroll_img_lib, 'no.PNG')
gashapon_finish = os.path.join(auto_reroll_img_lib, 'gashapon_finish.PNG')
defeat = os.path.join(auto_reroll_img_lib, 'defeat.PNG')

base_cat = os.path.join(auto_reroll_img_lib, 'base_cat.PNG')
wall_cat = os.path.join(auto_reroll_img_lib, 'wall_cat.PNG')
warrior_cat = os.path.join(auto_reroll_img_lib, 'warrior_cat.PNG')
leg_cat = os.path.join(auto_reroll_img_lib, 'leg_cat.PNG')

crazy_worker = os.path.join(auto_reroll_img_lib, 'crazy_worker.PNG')