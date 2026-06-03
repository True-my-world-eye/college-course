import pandas as pd

data = {
    '种类':['牧羊犬','雪纳瑞','柯基犬','柯基犬','田园犬','牧羊犬','田园犬','柯基犬'],
    '名称':['小德','小悠','土豆','面包','旺财','小边','田园猫','蛋黄派'],
    '年龄':[1.5,3.0,2.2,4.5,8.7,2.4,5.3,1.1],
    '体重':[25.0,17.8,11.6,13.4,22.2,31.7,18.7,9.5]
}
df = pd.DataFrame(data)

# (a)
print(df)

# (b)
print(df.iloc[0,0])
print(df.iloc[-1,-1])

# (c)
print(df.head(4))

# (d)
print(df.describe())

# (e)
arr = df.values
print(arr)