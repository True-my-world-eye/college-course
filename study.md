# 🧩 os 模块（文件 / 路径 / 文件夹）

| 函数 / 属性                       | 作用                                  |
| :-------------------------------- | :------------------------------------ |
| `os.path.join(path1, path2, ...)` | 安全拼接路径，自动加 `/` 或 `\`       |
| `os.path.exists(path)`            | 判断文件 / 文件夹是否存在             |
| `os.listdir(dir)`                 | 获取目录下所有文件 / 文件夹名（列表） |
| `os.mkdir(dir)`                   | 创建单层文件夹                        |
| `os.makedirs(dir)`                | 递归创建多层文件夹                    |
| `os.remove(file)`                 | 删除文件                              |
| `os.rename(old, new)`             | 重命名文件 / 文件夹                   |
| `os.path.isfile(path)`            | 判断是否为文件                        |
| `os.path.isdir(path)`             | 判断是否为文件夹                      |

## 【os 汇总演示代码】

```python
import os

# 1. 路径拼接
path = os.path.join("test", "a.txt")
print("拼接路径:", path)

# 2. 判断是否存在
print("是否存在:", os.path.exists(path))

# 3. 列出文件夹内容
print("当前目录文件:", os.listdir("."))

# 4. 创建文件夹
if not os.path.exists("mydir"):
    os.mkdir("mydir")

# 5. 判断是文件还是文件夹
print("是文件?", os.path.isfile("mydir"))
print("是文件夹?", os.path.isdir("mydir"))
```

------

# 🎲 random 模块（随机数）

| 函数                    | 作用                     |
| :---------------------- | :----------------------- |
| `random.randint(a, b)`  | 生成 [a,b] 随机整数      |
| `random.random()`       | 生成 [0,1) 随机小数      |
| `random.uniform(a, b)`  | 生成 [a,b] 随机小数      |
| `random.choice(seq)`    | 从序列中随机选 1 个      |
| `random.shuffle(list)`  | 打乱列表顺序（原地修改） |
| `random.sample(seq, k)` | 随机选 k 个不重复元素    |

## 【random 汇总演示代码】

```python
import random

# 1. 随机整数 0~10
print("randint(0,10):", random.randint(0, 10))

# 2. 0~1 随机小数
print("random():", random.random())

# 3. 指定范围小数
print("uniform(1,5):", random.uniform(1, 5))

# 4. 随机选一个
lst = [10, 20, 30, 40]
print("choice:", random.choice(lst))

# 5. 打乱列表
random.shuffle(lst)
print("shuffle 后:", lst)

# 6. 随机选2个
print("sample 2个:", random.sample(lst, 2))
```

------

# ⏱️time 模块（时间戳、延时）

| 函数               | 作用                   |
| :----------------- | :--------------------- |
| `time.time()`      | 获取当前时间戳（秒）   |
| `time.sleep(sec)`  | 程序暂停 sec 秒        |
| `time.ctime()`     | 获取可读当前时间       |
| `time.localtime()` | 获取本地时间（结构化） |

## 【time 汇总演示代码】

```python
import time

# 1. 时间戳
print("时间戳:", time.time())

# 2. 可读时间
print("当前时间:", time.ctime())

# 3. 延时1秒
print("等待1秒...")
time.sleep(1)
print("继续")

# 4. 本地时间结构体
print("本地时间:", time.localtime())
```

------

# 📅 datetime 模块（日期时间）

| 函数 / 类                      | 作用                         |
| :----------------------------- | :--------------------------- |
| `datetime.date.today()`        | 获取今天日期（年 - 月 - 日） |
| `datetime.datetime.now()`      | 获取当前完整时间             |
| `dt.strftime(格式)`            | 时间 → 格式化字符串          |
| `datetime.timedelta(days=...)` | 时间加减                     |

## 【datetime 汇总演示代码】

```python
import datetime

# 1. 今天日期
today = datetime.date.today()
print("today:", today)

# 2. 当前完整时间
now = datetime.datetime.now()
print("now:", now)

# 3. 格式化输出
fmt = now.strftime("%Y-%m-%d %H:%M:%S")
print("格式化:", fmt)

# 4. 时间加减（+1天）
next_day = now + datetime.timedelta(days=1)
print("明天此时:", next_day)
```

# csv 模块

| 函数 / 用法                     | 作用                                       |
| :------------------------------ | :----------------------------------------- |
| `csv.reader(f)`                 | 按行读取 CSV，返回迭代器，每行为列表       |
| `csv.DictReader(f)`             | 按行读取 CSV，每行转为字典（用第一行做键） |
| `csv.writer(f)`                 | 创建写入器，用于写 CSV                     |
| `csv.DictWriter(f, fieldnames)` | 字典方式写入 CSV                           |
| `writer.writerow (列表)`        | 写入一行（列表形式）                       |
| `writer.writerows (二维列表)`   | 一次性写入多行                             |
| `DictWriter.writeheader()`      | 写入表头（字段名行）                       |

## 【csv汇总演示代码】

```python
import csv

# ======================
# 1. 普通写入 CSV
# ======================
with open("test.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    # 写表头
    writer.writerow(["name", "age", "score"])
    # 写多行
    writer.writerows([
        ["张三", 18, 90],
        ["李四", 19, 85],
        ["王五", 20, 88]
    ])

# ======================
# 2. 普通读取 CSV
# ======================
print("=== 普通 reader 读取 ===")
with open("test.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# ======================
# 3. 字典方式写入
# ======================
with open("dict_test.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "age", "score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()  # 写表头
    writer.writerow({"name": "小明", "age": 18, "score": 95})
    writer.writerow({"name": "小红", "age": 19, "score": 92})

# ======================
# 4. 字典方式读取
# ======================
print("\n=== DictReader 读取 ===")
with open("dict_test.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
```

# zipfile 模块

| 函数 / 用法                                        | 作用                                 |
| :------------------------------------------------- | :----------------------------------- |
| `zipfile.ZipFile(文件, 'r', zipfile.ZIP_DEFLATED)` | **读取 / 打开** zip 压缩包           |
| `zipfile.ZipFile(文件, 'w', zipfile.ZIP_DEFLATED)` | **创建 / 写入** zip 压缩包           |
| `zipf.namelist()`                                  | 获取压缩包内**所有文件名列表**       |
| `zipf.extract(文件名, 路径)`                       | **解压单个文件**到指定路径           |
| `zipf.extractall(路径)`                            | **解压全部文件**到指定路径           |
| `zipf.write(文件路径)`                             | **往压缩包添加文件**                 |
| `zipf.close()`                                     | 关闭压缩包（推荐用 `with` 自动关闭） |
| `with zipfile.ZipFile(...) as zipf`                | 安全打开，自动关闭                   |

## zipfile 汇总测试代码

```python
import zipfile
import os

# ==========================
# 1. 创建一个 zip 压缩包
# ==========================
with zipfile.ZipFile("test.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    # 添加文件到压缩包
    zipf.write("test.csv")       # 添加单个文件
    zipf.write("dict_test.csv")  # 再添加一个

print("✅ 已创建压缩包 test.zip")

# ==========================
# 2. 查看压缩包内文件
# ==========================
with zipfile.ZipFile("test.zip", "r") as zipf:
    file_list = zipf.namelist()
    print("\n压缩包内的文件：", file_list)

# ==========================
# 3. 解压全部文件
# ==========================
if not os.path.exists("unzip_dir"):
    os.mkdir("unzip_dir")

with zipfile.ZipFile("test.zip", "r") as zipf:
    zipf.extractall("unzip_dir")  # 解压全部

print("✅ 已解压到 unzip_dir 文件夹")

# ==========================
# 4. 解压单个文件
# ==========================
with zipfile.ZipFile("test.zip", "r") as zipf:
    zipf.extract("test.csv", "single_unzip")

print("✅ 已单独解压 test.csv 到 single_unzip")
```

# 🔐 hashlib 模块（哈希 / 加密）

| 函数 / 用法               | 作用                                        |
| ------------------------- | ------------------------------------------- |
| `hashlib.md5()`           | 创建 MD5 哈希对象（128 位，不推荐加密场景） |
| `hashlib.sha1()`          | 创建 SHA1 哈希对象（160 位）                |
| `hashlib.sha256()`        | 创建 SHA256 哈希对象（256 位，常用）        |
| `hash_obj.update(字节串)` | 向哈希对象传入待加密的字节数据              |
| `hash_obj.hexdigest()`    | 获取十六进制格式的哈希结果（字符串）        |
| `hash_obj.digest()`       | 获取二进制格式的哈希结果                    |

## 【hashlib 汇总演示代码】

```python
import hashlib

# ======================
# 1. 基础使用（MD5）
# ======================
# 注意：待加密内容需转为字节串（encode）
text = "hello world"
md5_obj = hashlib.md5()
md5_obj.update(text.encode("utf-8"))
md5_result = md5_obj.hexdigest()
print("MD5 结果:", md5_result)  # 输出 32位十六进制字符串

# ======================
# 2. SHA256（推荐）
# ======================
sha256_obj = hashlib.sha256()
sha256_obj.update(text.encode("utf-8"))
sha256_result = sha256_obj.hexdigest()
print("SHA256 结果:", sha256_result)  # 输出 64位十六进制字符串

# ======================
# 3. 分块更新（大文件场景）
# ======================
big_text = "Python hashlib 分块加密演示"
sha1_obj = hashlib.sha1()
# 模拟大文件分块读取，多次update
sha1_obj.update(big_text[:10].encode("utf-8"))
sha1_obj.update(big_text[10:].encode("utf-8"))
sha1_result = sha1_obj.hexdigest()
print("SHA1 分块结果:", sha1_result)

# ======================
# 4. 二进制 digest 结果
# ======================
md5_bin = md5_obj.digest()
print("MD5 二进制结果:", md5_bin)  # 输出 bytes 类型
print("二进制长度:", len(md5_bin))  # MD5 二进制长度为16字节

# ======================
# 5. 实用封装（文件哈希计算）
# ======================
def get_file_hash(file_path, algorithm="sha256"):
    """
    计算文件的哈希值
    :param file_path: 文件路径
    :param algorithm: 哈希算法（md5/sha1/sha256）
    :return: 十六进制哈希结果
    """
    if algorithm not in ["md5", "sha1", "sha256"]:
        raise ValueError("不支持的哈希算法")
    
    hash_obj = hashlib.new(algorithm)
    with open(file_path, "rb") as f:
        # 分块读取大文件，避免内存溢出
        while chunk := f.read(4096):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

# 测试文件哈希计算（需确保文件存在，可替换为实际文件路径）
# print("文件 SHA256 哈希:", get_file_hash("test.csv"))
```

**补充说明**

1. **编码要求**：`update()` 仅接收字节串（bytes），字符串需通过 `encode("utf-8")` 转换；
2. **哈希特性**：相同内容始终生成相同哈希值，内容微小变化哈希值完全不同（雪崩效应）；
3. **安全场景**：MD5/SHA1 已不推荐用于密码加密等安全场景，优先使用 SHA256/SHA512；
4. **常用场景**：文件完整性校验、密码存储（需加盐）、数据去重等。

# 🧮 numpy 模块（数值计算基础）

| 函数 / 类 / 属性               | 作用                                    |
| ------------------------------ | --------------------------------------- |
| `numpy.array(seq)`             | 创建 numpy 数组（ndarray）              |
| `np.zeros(shape)`              | 创建全 0 数组，shape 为元组（如 (3,4)） |
| `np.ones(shape)`               | 创建全 1 数组                           |
| `np.arange(start, end, step)`  | 生成有序数组（类似 range，支持小数）    |
| `np.linspace(start, end, num)` | 生成指定数量的等间隔数组                |
| `arr.shape`                    | 数组维度（返回元组）                    |
| `arr.dtype`                    | 数组数据类型                            |
| `arr.reshape(new_shape)`       | 重塑数组维度（不改变原数组）            |
| `np.mean(arr)` / `arr.mean()`  | 计算数组均值                            |
| `np.sum(arr)` / `arr.sum()`    | 计算数组总和                            |
| `np.max(arr)` / `arr.max()`    | 数组最大值                              |
| `np.min(arr)` / `arr.min()`    | 数组最小值                              |
| `np.dot(arr1, arr2)`           | 矩阵点乘（线性代数）                    |
| `arr[行, 列]`                  | 数组索引 / 切片（支持多维）             |

## 【numpy 汇总演示代码】

```python
import numpy as np

# 1. 创建数组
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.zeros((3, 4))  # 3行4列全0数组
arr3 = np.ones((2, 3))   # 2行3列全1数组
arr4 = np.arange(0, 10, 2)  # [0 2 4 6 8]
arr5 = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]

print("基础数组:", arr1)
print("全0数组:\n", arr2)
print("数组形状:", arr2.shape)  # (3, 4)

# 2. 数组操作
arr_reshape = arr1.reshape((5, 1))  # 转为5行1列
print("重塑后:\n", arr_reshape)

# 3. 数值计算
print("均值:", arr1.mean())  # 3.0
print("总和:", np.sum(arr1))  # 15
print("最大值:", arr1.max())  # 5

# 4. 矩阵运算
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
dot_result = np.dot(mat1, mat2)
print("矩阵点乘:\n", dot_result)

# 5. 数组切片
print("切片取前3个元素:", arr1[:3])  # [1 2 3]
print("取矩阵第一行:", mat1[0, :])  # [1 2]
```

# numpy.random

 是 NumPy 中专门用于生成随机数的子模块

核心函数 / 方法汇总

| 函数                                           | 作用                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| `np.random.rand(d0, d1, ...)`                  | 生成 [0,1) 均匀分布的随机数，参数指定数组维度（如 `rand(3,4)` 生成 3 行 4 列） |
| `np.random.randn(d0, d1, ...)`                 | 生成标准正态分布（均值 0，标准差 1）的随机数，维度规则同 `rand` |
| `np.random.randint(low, high=None, size=None)` | 生成 [low, high) 整数，size 指定输出形状（如 `randint(0,10,(2,3))`） |
| `np.random.choice(a, size=None, replace=True)` | 从数组 / 序列 `a` 中随机抽样，size 指定抽样形状，replace 控制是否可重复 |
| `np.random.shuffle(x)`                         | 原地打乱数组 `x` 的第一维（对多维数组仅打乱行）              |
| `np.random.permutation(x)`                     | 返回打乱后的数组副本（不修改原数组），x 为整数时生成打乱的 0~x-1 序列 |
| `np.random.uniform(low, high, size=None)`      | 生成 [low, high) 均匀分布随机数                              |
| `np.random.normal(loc=0, scale=1, size=None)`  | 生成正态分布随机数（loc = 均值，scale = 标准差）             |
| `np.random.seed(seed)`                         | 设置随机数种子（固定随机结果，便于复现）                     |

```python
import numpy as np

# ======================
# 1. 基础随机数生成
# ======================
# [0,1) 均匀分布（3行2列）
rand_arr = np.random.rand(3, 2)
print("rand (3x2 均匀分布):\n", rand_arr)

# 标准正态分布（2行3列）
randn_arr = np.random.randn(2, 3)
print("\nrandn (2x3 标准正态):\n", randn_arr)

# 整数随机数 [0, 10)，生成1维数组（长度5）
randint_arr = np.random.randint(0, 10, size=5)
print("\nrandint [0,10) 1维:", randint_arr)

# 整数随机数 [5, 15)，生成2维数组（2x4）
randint_2d = np.random.randint(5, 15, size=(2, 4))
print("\nrandint [5,15) 2x4:\n", randint_2d)

# ======================
# 2. 自定义分布随机数
# ======================
# [1, 5) 均匀分布（1x4）
uniform_arr = np.random.uniform(1, 5, size=4)
print("\nuniform [1,5):", uniform_arr)

# 正态分布（均值=2，标准差=0.5，3x3）
normal_arr = np.random.normal(loc=2, scale=0.5, size=(3, 3))
print("\nnormal (均值2, 标准差0.5):\n", normal_arr)

# ======================
# 3. 随机抽样/打乱
# ======================
# 从序列中随机选值
choice_1d = np.random.choice([10, 20, 30, 40], size=3)  # 可重复抽样
print("\nchoice 可重复抽样:", choice_1d)

choice_no_replace = np.random.choice([10, 20, 30, 40], size=3, replace=False)  # 不重复抽样
print("choice 不重复抽样:", choice_no_replace)

# 打乱数组（原地修改）
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print("\nshuffle 后（原地）:", arr)

# 打乱数组（返回副本，不修改原数组）
arr2 = np.array([[1,2], [3,4], [5,6]])
perm_arr = np.random.permutation(arr2)
print("\npermutation 后（副本）:\n", perm_arr)
print("原数组未变:\n", arr2)

# ======================
# 4. 固定随机种子（结果可复现）
# ======================
np.random.seed(42)  # 固定种子
print("\n固定种子后 rand:", np.random.rand(3))  # 每次运行结果相同
np.random.seed(42)
print("再次运行同种子 rand:", np.random.rand(3))  # 和上一行结果一致
```

------

# 🔬 scipy 模块（科学计算 / 高级算法）

| 子模块 / 函数     | 作用                               |
| ----------------- | ---------------------------------- |
| `scipy.special`   | 特殊函数（贝塞尔、伽马、阶乘等）   |
| `scipy.optimize`  | 优化算法（最小值、方程求解）       |
| `scipy.integrate` | 积分计算（定积分、常微分方程）     |
| `scipy.stats`     | 统计分析（概率分布、假设检验）     |
| `scipy.ndimage`   | 多维图像处理（滤波、插值）         |
| `scipy.fftpack`   | 快速傅里叶变换                     |
| `scipy.linalg`    | 线性代数高级操作（逆矩阵、特征值） |

## 【scipy 汇总演示代码】

```python
import numpy as np
from scipy import optimize, integrate, stats, linalg

# 1. 优化：求解函数最小值
def func(x):
    return x**2 + 10*np.sin(x)

# 找最小值（初始猜测值x0=0）
result = optimize.minimize(func, x0=0)
print("函数最小值点:", result.x[0])  # 约-1.306

# 2. 积分：计算定积分 ∫(0→1) x^2 dx
integral_result, error = integrate.quad(lambda x: x**2, 0, 1)
print("定积分结果:", integral_result)  # 0.33333333333333337

# 3. 统计：正态分布
norm_dist = stats.norm(loc=0, scale=1)  # 均值0，标准差1
# 计算概率密度（x=0处）
pdf_val = norm_dist.pdf(0)
# 计算累计概率 P(X ≤ 1)
cdf_val = norm_dist.cdf(1)
print("正态分布PDF(0):", pdf_val)  # ~0.3989
print("正态分布CDF(1):", cdf_val)  # ~0.8413

# 4. 线性代数：求逆矩阵
mat = np.array([[1, 2], [3, 4]])
inv_mat = linalg.inv(mat)
print("逆矩阵:\n", inv_mat)

# 5. 解方程：求解 2x + 5 = 0
def eq(x):
    return 2*x + 5

root = optimize.root(eq, x0=0)
print("方程解:", root.x[0])  # -2.5
```

------

# 📊 pandas 模块（数据处理 / 分析）

| 类 / 函数 / 方法         | 作用                                   |
| ------------------------ | -------------------------------------- |
| `pandas.Series(数据)`    | 创建一维序列（带索引）                 |
| `pandas.DataFrame(数据)` | 创建二维数据表（行 / 列索引）          |
| `df.read_csv(文件路径)`  | 读取 CSV 文件到 DataFrame              |
| `df.to_csv(文件路径)`    | 将 DataFrame 写入 CSV 文件             |
| `df.head(n)`             | 查看前 n 行数据（默认 5 行）           |
| `df.info()`              | 查看数据基本信息（列类型、非空值）     |
| `df.describe()`          | 数值列统计摘要（均值、标准差、分位数） |
| `df.dropna()`            | 删除含缺失值的行                       |
| `df.fillna(值)`          | 填充缺失值                             |
| `df.groupby(列名)`       | 按列分组统计                           |
| `df.merge(df2)`          | 数据表连接（类似 SQL join）            |
| `df.loc[行标签, 列标签]` | 按标签索引数据                         |
| `df.iloc[行号, 列号]`    | 按位置索引数据                         |

## 【pandas 汇总演示代码】

```python
import pandas as pd
import numpy as np

# 1. 创建数据结构
# 一维 Series
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
# 二维 DataFrame
df = pd.DataFrame({
    "name": ["张三", "李四", "王五", "赵六"],
    "age": [18, 19, np.nan, 21],
    "score": [90, 85, 88, 92]
})

print("Series:\n", s)
print("DataFrame:\n", df)

# 2. 数据查看与清洗
print("前2行:", df.head(2))
print("数据信息:")
df.info()
# 填充缺失值（年龄列用均值填充）
df["age"] = df["age"].fillna(df["age"].mean())
print("填充缺失值后:\n", df)

# 3. 数据统计
print("统计摘要:\n", df.describe())
# 按分数分组（示例：分高低分）
df["score_level"] = df["score"].apply(lambda x: "高" if x>=90 else "中")
grouped = df.groupby("score_level")["age"].mean()
print("分组均值:\n", grouped)

# 4. 数据索引
print("按标签取张三:", df.loc[df["name"]=="张三", "score"])
print("按位置取第2行第3列:", df.iloc[1, 2])

# 5. 读写CSV
df.to_csv("student.csv", index=False, encoding="utf-8")
df_read = pd.read_csv("student.csv", encoding="utf-8")
print("读取CSV:\n", df_read)
```

------

# 📈 matplotlib 模块（数据可视化）

| 函数 / 方法                 | 作用                     |
| --------------------------- | ------------------------ |
| `matplotlib.pyplot`         | 核心绘图模块（简称 plt） |
| `plt.plot(x, y)`            | 绘制折线图               |
| `plt.scatter(x, y)`         | 绘制散点图               |
| `plt.bar(x, height)`        | 绘制柱状图               |
| `plt.hist(x)`               | 绘制直方图               |
| `plt.pie(x)`                | 绘制饼图                 |
| `plt.xlabel/ylabel(文本)`   | 设置 x/y 轴标签          |
| `plt.title(文本)`           | 设置图表标题             |
| `plt.legend()`              | 显示图例                 |
| `plt.grid(True)`            | 显示网格线               |
| `plt.savefig(路径)`         | 保存图片到文件           |
| `plt.show()`                | 显示图表                 |
| `plt.subplot(行, 列, 位置)` | 创建子图（多图布局）     |

## 【matplotlib 汇总演示代码】

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 设置中文显示（解决中文乱码）
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 黑体
plt.rcParams["axes.unicode_minus"] = False    # 解决负号显示问题

# 1. 折线图
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 4))  # 设置画布大小
plt.plot(x, y, label="sin(x)", color="red", linestyle="--")
plt.xlabel("x 轴")
plt.ylabel("y 轴")
plt.title("正弦函数折线图")
plt.legend()
plt.grid(True)
plt.show()

# 2. 柱状图
categories = ["A", "B", "C", "D"]
values = [20, 35, 30, 25]
plt.figure(figsize=(6, 4))
plt.bar(categories, values, color=["blue", "green", "orange", "purple"])
plt.title("分类数据柱状图")
plt.ylabel("数值")
plt.show()

# 3. 散点图
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)
plt.figure(figsize=(6, 4))
plt.scatter(x_scatter, y_scatter, c=colors, s=sizes, alpha=0.7)
plt.title("随机散点图")
plt.show()

# 4. 子图（多图布局）
plt.figure(figsize=(10, 6))
# 子图1：饼图
plt.subplot(2, 2, 1)
pie_data = [15, 30, 45, 10]
plt.pie(pie_data, labels=["甲", "乙", "丙", "丁"], autopct="%1.1f%%")
plt.title("饼图")

# 子图2：直方图
plt.subplot(2, 2, 2)
hist_data = np.random.randn(1000)
plt.hist(hist_data, bins=30, color="skyblue")
plt.title("直方图")

# 子图3：折线图（pandas数据）
plt.subplot(2, 2, 3)
df_plot = pd.DataFrame({"x": [1,2,3,4,5], "y": [10, 15, 12, 18, 14]})
plt.plot(df_plot["x"], df_plot["y"], marker="o", color="green")
plt.title("DataFrame 折线图")

plt.tight_layout()  # 自动调整子图间距
plt.show()

# 5. 保存图片
plt.figure(figsize=(6, 4))
plt.plot(x, np.cos(x), label="cos(x)")
plt.title("余弦函数")
plt.savefig("cos_plot.png", dpi=100, bbox_inches="tight")  # 保存图片
print("图片已保存为 cos_plot.png")
```