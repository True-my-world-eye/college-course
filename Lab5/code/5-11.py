import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Lab5/data/user_data.xls")

df["访问日期"]=pd.to_datetime(df["访问日期"],format="%Y-%m-%d")
df["月份"]=df["访问日期"].dt.month

month_sum=df.groupby("月份")["购买金额"].sum().reset_index()
print(month_sum)

plt.bar(month_sum["月份"],month_sum["购买金额"])
plt.xlabel("月份")
plt.ylabel("总金额")
plt.show()