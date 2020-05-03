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
构造初始数据矩阵和数据标签，由于时间不是全部连续的，每个月只有前20天，将每个月单独处理。
时间窗口为10，前九天的数据为X，第十天的PM2.5为y,
"""
data_raw = pd.read_csv(raw_path + "train.csv", encoding="big5")
data_raw = data_raw.drop(["site"], axis=1)
data_raw["date_num"] = data_raw["date"].apply(lambda x: time.strftime('%j', time.strptime(x, '%Y/%m/%d')))
data_raw["month"] = data_raw["date"].apply(lambda x: re.split(r"/", x)[1])

item = data_raw["item"][:18]
# print(item)
train_df = pd.DataFrame()
label_list = []
for i in data_raw.groupby("month"):
    print(i[0])
    month_df = pd.DataFrame()
    for j in i[1].groupby("date_num"):
        j = j[1].reset_index(drop=True)
        j = j.drop(["item", "date", "date_num", "month"], axis=1)
        month_df = pd.concat([month_df, j], axis=1)
    # print(month_df)
    df_t = pd.DataFrame(month_df.values.T, columns=item)
    df_t = df_t.drop(["RAINFALL", "CH4"], axis=1)

    for idx, _ in df_t.iterrows():
        # print(idx, i)
        single_sample_list = pd.DataFrame()
        if idx + 10 > 478:
            break
        for j in range(9):
            single_sample_list = pd.concat([single_sample_list, pd.DataFrame(df_t.iloc[j + idx, :].values.T)], axis=0)
        # print(single_sample_list)
        single_sample_list = single_sample_list.reset_index(drop=True)
        label_list.append(eval(df_t.iloc[10 + idx, 8]))
        train_df = pd.concat([train_df, single_sample_list], axis=1)
    # break
    # 跳出循环
# print(pd.DataFrame(train_df.values.T))
# print(len(label_list))
pk.dump(pd.DataFrame(train_df.values.T), file=open("./temp/train.pkl", "wb"))
pk.dump(label_list, file=open("./temp/label.pkl", "wb"))
