from sikulix4python import *

if __name__ == '__main__':  
    screen = Screen(2)

    img_lib_path            = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "img_lib")     # 圖庫
    img_green_catnip_seed = os.path.join(img_lib_path, 'green_catnip_seed')
    img_green_catnip_seed1 = os.path.join(img_lib_path, 'green_catnip_seed1')
    img_green_catnip_seed2 = os.path.join(img_lib_path, 'green_catnip_seed2')
    img_green_catnip_seed3 = os.path.join(img_lib_path, 'green_catnip_seed3')
    img_green_catnip_seed4 = os.path.join(img_lib_path, 'green_catnip_seed4')

    img_battle_start = os.path.join(img_lib_path, 'battle_start')
    img_nuonuo_cat = os.path.join(img_lib_path, 'nuonuo_cat')

    # if screen.exists(img_green_catnip_seed1):
    #     print('貓薄荷種子')
    # else:
    #     print('貓薄荷')
    
    # print(screen.exists(img_nuonuo_cat))
    if screen.exists(img_nuonuo_cat):
        screen.click(img_nuonuo_cat)