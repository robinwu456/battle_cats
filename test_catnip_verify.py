from sikulix4python import *

if __name__ == '__main__':  
    screen = Screen(1)

    img_lib_path            = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "img_lib")     # 圖庫
    img_green_catnip_seed = os.path.join(img_lib_path, 'green_catnip_seed')
    img_green_catnip_seed1 = os.path.join(img_lib_path, 'green_catnip_seed1')
    img_green_catnip_seed2 = os.path.join(img_lib_path, 'green_catnip_seed2')
    img_green_catnip_seed3 = os.path.join(img_lib_path, 'green_catnip_seed3')
    img_green_catnip_seed4 = os.path.join(img_lib_path, 'green_catnip_seed4')

    if screen.exists(img_green_catnip_seed1):
        print('貓薄荷種子')
    else:
        print('貓薄荷')