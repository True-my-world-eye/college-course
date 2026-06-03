import numpy as np
import pandas as pd

df=pd.read_excel('Lab5/data/data.xls')

# 计算人均排放
df["CO2 per Capita"] = df["CO2_Emissions"] / df["Population"]

# 排放量最高国家
max_country = df.loc[df["CO2_Emissions"].idxmax()]
print("最高国家：\n", max_country)