# -*- coding:utf-8 -*-
import argparse
from time import sleep
from sikulix4python import *
from auto_stage_base import *
from all_cats import *

class OtherStage(AutoStageBase):
    use_cats = [
        crazy_normal_cat,
        crazy_wall_cat,
        wall_cat,
        pole_cat,
    ]

    def __init__(self, args):
        super().__init__(args)