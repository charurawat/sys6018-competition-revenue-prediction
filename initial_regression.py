#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

def load_df(csv_path='./all/train.csv', nrows=None):
    JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']
    df = pd.read_csv(csv_path, dtype={'fullVisitorId': 'str'}, nrows=nrows)
    for column in JSON_COLUMNS:
        df = df.join(pd.DataFrame(df.pop(column).apply(pd.io.json.loads).values.tolist(), index=df.index))
    return df

n_obs = 1000

df_train_small = load_df(nrows=n_obs)
df_train_small

df_test_small = load_df(csv_path='./all/test.csv', nrows = n_obs)

    
