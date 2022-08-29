# -*- coding:utf-8 -*-
import os
from auto_stage_base import AutoStageBase
from sikulix4python import *
from all_cats import *

class PurpleCatnip(AutoStageBase):
    use_cats = [
        nuonuo_cat,
        dance_cat,
        twins_cat,
        horse_cat,
        nurse_cat,
    ]

    def __init__(self, args):
        super().__init__(args)      