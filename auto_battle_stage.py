# -*- coding:utf-8 -*-
import argparse
from datetime import datetime
from other_stage import OtherStage

from other_stage import OtherStage

# 腳本對應
dict_catnip_func = {
    'other': { 'name': '其他', 'script_class': OtherStage },
}

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--catnip-color", help="要刷貓薄荷的顏色")
    parser.add_argument("-o", "--run-out-energy", help="重複直到體力用完", action="store_true")
    parser.add_argument("-f", "--use-flags", type=int, default=0, help="用旗子數量")
    parser.add_argument("-a", "--stage-attack", help="直接打關卡", action="store_true")
    parser.add_argument("-n", "--count-catnip", type=int, default=0, help="重複直到拿到貓薄荷數")
    parser.add_argument("-s", "--count-catnip-seeds", type=int, default=0, help="重複直到拿到貓薄荷種子數")
    args = parser.parse_args()
    
    # 必須輸入要刷的貓薄荷顏色
    if not args.catnip_color:
        print('請輸入要刷的貓薄荷顏色')
        exit()

    if args.catnip_color:
        print (f"刷的貓薄荷顏色: {dict_catnip_func[args.catnip_color]['name']}")
    if args.use_flags:
        print (f"使用旗子數: {args.use_flags}")
        # args.run_out_energy = True
    if args.run_out_energy:
        print (f"體力使用完畢: {args.run_out_energy}")    
    if args.stage_attack:
        print (f"直接打關卡: {args.stage_attack}")    
    if args.count_catnip:
        print (f"需取得貓薄荷數: {args.count_catnip}")
        args.run_out_energy = True
        args.use_flags = 999
    if args.count_catnip_seeds:
        print (f"需取得貓薄荷種子數: {args.count_catnip_seeds}") 
        args.run_out_energy = True   
        args.use_flags = 999
    
    # 開始刷貓薄荷
    auto_catnip = dict_catnip_func[args.catnip_color]['script_class'](args)
    try:
        auto_catnip.start(auto_catnip.use_cats_method, auto_catnip.use_cats)
    except Exception as ex:
        auto_catnip.debug_log(ex)