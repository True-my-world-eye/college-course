# Lab5 Python 科学计算实践 — 知识文档

## 1. 实验目标概览
- 掌握 NumPy 数组的创建、索引、切片和运算
- 学会用 Pandas 处理表格数据（DataFrame）
- 学会用 Matplotlib 和 Seaborn 绘制图表
- 了解 Scipy 的基本用法

---

## 2. 核心知识点

### 2.1 NumPy 数组

```python
import numpy as np

# 创建数组
arr = np.array([1, 2, 3])
zeros = np.zeros((3, 4))      # 3行4列全0
ones = np.ones((2, 3))        # 2行3列全1
rand = np.random.randn(9, 10) # 9x10 标准正态分布
uniform = np.random.uniform(0, 1, 20000)  # 20000个[0,1)均匀分布
normal = np.random.normal(3, 2, 20000)    # 20000个 N(3,2) 正态分布
```

#### 索引和切片

```python
arr = np.random.randn(9, 10)
arr[1, 4]          # 第2行第5列
arr[2:5, 3:6]      # 第3-5行，第4-6列（切片）
arr[2:5, [0,1,3]] # 第3-5行，第1、2、4列（混合索引）

# 布尔索引（超级好用！）
arr[arr > 1] = 10.0    # 将所有大于1的元素替换为10
arr[arr < -1] = -10.0  # 将所有小于-1的元素替换为-10
```

#### 数组运算

```python
A + C            # 逐元素加法
A / B            # 逐元素除法
A * B            # 逐元素乘法（不是矩阵乘法！）
np.dot(A, B)     # 内积/点积
np.median(B)     # 中位数
np.std(B)        # 标准差
np.percentile(B, [25, 75])  # 四分位数
```

#### 矩阵操作

```python
mat = np.random.randn(1000, 1000)
min_val = mat.min()
max_val = mat.max()
# 正则化：将数据缩放到 [0, 1]
mat_norm = (mat - min_val) / (max_val - min_val)

# 按行减去均值
row_mean = mat.mean(axis=1, keepdims=True)
new_mat = mat - row_mean

# 保存和读取
np.savetxt("data.csv", mat, delimiter=",", fmt="%.3f")
data = np.loadtxt("data.csv", delimiter=",")
```

### 2.2 Pandas DataFrame

```python
import pandas as pd

# 从字典创建
data = {"name": ["Alice", "Bob"], "score": [85, 92]}
df = pd.DataFrame(data)

# 读取文件
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xls")
df = pd.read_parquet("file.parquet")

# 探索数据
df.head(10)        # 前10行
df.shape           # (行数, 列数)
df.info()          # 列信息、类型、缺失值
df.describe()      # 统计摘要
df.values          # 转为 NumPy 数组

# 数据操作
df["新列"] = df["列A"] / df["列B"]   # 添加新列
df.groupby("月份")["金额"].sum()      # 分组聚合
df.loc[df["列A"].idxmax()]           # 某列最大值所在行
```

### 2.3 Matplotlib 绘图

```python
import matplotlib.pyplot as plt

# 折线图
plt.plot(x, y1, label="y=x²")
plt.plot(x, y2, label="y=ln(x)")
plt.legend()
plt.title("标题")
plt.xlabel("X轴")
plt.ylabel("Y轴")
plt.show()

# 直方图
plt.hist(data, bins=100)

# 柱状图
plt.bar(x, y)
```

### 2.4 Seaborn 绘图（更美观）

```python
import seaborn as sns

sns.set(style="darkgrid")                    # 设置风格
sns.scatterplot(x="列A", y="列B", data=df)   # 散点图
sns.lineplot(x="列A", y="列B", data=df)      # 折线图
sns.barplot(x=..., y=...)                    # 柱状图
sns.histplot(data["列"])                     # 直方图
```

### 2.5 日期时间处理

```python
df["日期"] = pd.to_datetime(df["日期"], format="%Y-%m-%d")
df["月份"] = df["日期"].dt.month
```

---

## 3. 初学者常见坑

- **NumPy 乘法**：`A * B` 是逐元素乘，不是矩阵乘法。矩阵乘法用 `np.dot(A, B)` 或 `@`
- **Pandas 路径**：`read_csv` 参数是文件路径，用相对路径时注意当前工作目录
- **`plt.show()` 阻塞**：程序会停住直到关闭图表窗口
- **Seaborn 中文乱码**：需要设置中文字体 `sns.set(font='SimHei')`
