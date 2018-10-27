#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import os
#import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
#from pandas.io.json import json_normalize
#from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV
#from sklearn.model_selection import KFold
#import math


def load_df(csv_path='./all/train.csv', nrows=None):
    JSON_COLUMNS = ['device', 'geoNetwork', 'totals', 'trafficSource']
    df = pd.read_csv(csv_path, dtype={'fullVisitorId': 'str'}, nrows=nrows)
    for column in JSON_COLUMNS:
        df = df.join(pd.DataFrame(df.pop(column).apply(pd.io.json.loads).values.tolist(), index=df.index))
    return df

n_obs = 50000

df_train = load_df(nrows=n_obs)
#df_test = load_df(csv_path='./all/test.csv', nrows = n_obs)

df_train.transactionRevenue = [float(x) if (float(x) > 0) else 0 for x in df_train.transactionRevenue]

df_train[['hits','pageviews']] = df_train[['hits','pageviews']].apply(pd.to_numeric)


by_user_id = df_train.groupby(['fullVisitorId', 'country'])[['hits', 'pageviews', "transactionRevenue"]].sum().reset_index().rename_axis(None, axis=1)

by_user_id.transactionRevenue = [np.log(x) if x > 0 else 0 for x in by_user_id.transactionRevenue]

#x_values = pd.concat([df_train.hits, df_train.pageviews], axis = 1)




