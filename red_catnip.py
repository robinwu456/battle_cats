# -*- coding:utf-8 -*-
import argparse
from time import sleep
from sikulix4python import *
from catnip_base import *
from all_cats import *

class RedCatnip(CatnipBase):
    use_cats = [
        bath_cat,
        dance_cat,
        machine_cat,
        boat_cat,
        snow_cat,
        bahamut_cat,
    ]

    def __init__(self, args):
        super().__init__(args)      