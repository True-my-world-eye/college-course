import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "日期":["2025-04-01","2025-04-02","2025-04-03","2025-04-04","2025-04-05","2025-04-06","2025-04-07"],
    "访问数":[320,450,510,390,620,480,560],
    "注册数":[120,180,200,140,260,200,240],
    "下单数":[45,70,85,50,110,90,100],
    "成交额":[9000,14000,16000,10000,21000,18000,19500]
}

df = pd.DataFrame(data)
print(df)

df["转化率"]=(df["下单数"]/df["访问数"]).round(2)
print(df)


plt.plot(df["日期"],df["成交额"],label="成交额",marker="o")
plt.title("日期-成交额")
plt.show()

mean_val=np.mean(df["成交额"])
std_val=np.std(df["成交额"])
print("均值", mean_val, "标准差", std_val)