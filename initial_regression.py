#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os
os.chdir('/Users/Beni/Desktop/Fall_UVA/SYS6018/Competitions/comp_4/sys6018-competition-revenue-prediction')

n_obs = 100

test_data = pd.read_csv('./all/train.csv', nrows = n_obs)
test_data
