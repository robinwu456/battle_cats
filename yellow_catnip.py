# -*- coding:utf-8 -*-
import argparse
from time import sleep
from sikulix4python import *
from catnip_base import *
from all_cats import *

class YellowCatnip(CatnipBase):
    use_cats = [
        noodle_cat,
        pole_cat,
        rockband_cat,
        dance_cat,
        bahamut_cat,
    ]

    def __init__(self, args):
        super().__init__(args)