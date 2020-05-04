"""
package
"""
import pandas as pd
from pandas import DataFrame as df
from pandas import Series
import time
import re
import pickle as pk

"""
环境变量
"""
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 100)

raw_path = "./raw/"

"""
..
"""
# columns
data_raw = pd.read_csv(raw_path + "test.csv", encoding="big5")

for i in data_raw.groupby("id"):
    df_t = pd.DataFrame(i[1].values.T)
    df_t = df_t.drop(df_t.index[0])

    df_t.columns = df_t.iloc[0, :]
    df_t = df_t.drop(df_t.index[0])
    df_t.reset_index(inplace=True)
    df_t= df_t.drop(["RAINFALL", "CH4"], axis=1)
    print(df_t)
