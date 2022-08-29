# -*- coding:utf-8 -*-
import argparse
from time import sleep
from sikulix4python import *
from auto_stage_base import *
from all_cats import *

class GreenCatnip(AutoStageBase):
    use_cats = [
        # swim_cat,
        octopus_cat,
        dance_cat,
        dragon_cat,
        pole_cat,
        # bahamut_cat,
    ]

    def __init__(self, args):
        super().__init__(args)

    # def use_cats_method(self, use_cats):

    #     for cat in use_cats:
    #         try:
    #             if screen.exists(cat):
    #                 screen.click(cat)
    #         except Exception as ex:
    #             print(ex)
    #             if ex is KeyboardInterrupt:
    #                 return
    #             pass