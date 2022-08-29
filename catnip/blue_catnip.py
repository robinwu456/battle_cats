# -*- coding:utf-8 -*-
import argparse
from time import sleep
from sikulix4python import *
from auto_stage_base import *
from all_cats import *

class BlueCatnip(AutoStageBase):
    use_cats = [
        leg_cat,
        pole_cat,
        machine_cat,
        twins_cat,
        bahamut_cat,
    ]

    def __init__(self, args):
        super().__init__(args)