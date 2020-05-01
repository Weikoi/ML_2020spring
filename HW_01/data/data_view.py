"""
package
"""
import pandas as pd

"""
环境变量
"""
raw_path = "./raw/"

"""

"""
data_raw = pd.read_csv(raw_path + "train.csv", encoding="big5")
data_raw = data_raw.drop(["site"], axis=1)

for i in data_raw.groupby("date"):
    print(i)
