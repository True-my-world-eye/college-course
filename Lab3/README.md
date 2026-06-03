# Lab3 文件操作与数据存取 — 知识文档

## 1. 实验目标概览
- 掌握文件的打开、读取、写入
- 学会 `os` 模块进行文件和目录管理
- 理解 pickle 模块的数据持久化
- 了解 CSV 文件处理和 logging 日志

---

## 2. 核心知识点

### 2.1 文件操作基础

#### 打开模式

| 模式 | 说明 |
|------|------|
| `"r"` | 只读（默认） |
| `"w"` | 写入（覆盖已有内容） |
| `"a"` | 追加（在文件末尾添加） |
| `"rb"` | 二进制读取（用于图片、pickle） |
| `"wb"` | 二进制写入 |

#### 读取方式

```python
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()        # 全部读取为字符串
    line = f.readline()       # 读取一行
    lines = f.readlines()     # 读取所有行，返回列表
    # 或者直接遍历（推荐，省内存）
    for line in f:
        print(line.strip())
```

**务必使用 `with ... as` 语法**：它会自动关闭文件，避免资源泄漏。

#### 写入方式

```python
with open("out.txt", "w", encoding="utf-8") as f:
    f.write("Hello\n")        # 写入字符串
    f.writelines(["a\n", "b\n"])  # 写入多行
```

### 2.2 os 模块

```python
import os

os.path.exists(path)    # 判断文件/文件夹是否存在
os.path.isfile(path)    # 判断是否是文件
os.path.isdir(path)     # 判断是否是文件夹
os.mkdir("newdir")      # 创建单层目录
os.makedirs("a/b/c")    # 递归创建多层目录
os.listdir(".")         # 列出当前目录所有文件
os.path.getctime(path)  # 获取文件创建时间（时间戳）
```

### 2.3 shutil 模块（文件操作高级版）

```python
import shutil

shutil.copyfile(src, dst)    # 复制文件
shutil.move(src, dst)        # 移动文件/重命名
```

### 2.4 pickle 模块（数据持久化）

可以把 Python 对象保存到文件，下次再读回来。

```python
import pickle

# 保存
data = [func_name, file_list]
with open("data.pkl", "wb") as f:    # 注意 'wb' 二进制写入
    pickle.dump(data, f)

# 加载
with open("data.pkl", "rb") as f:    # 注意 'rb' 二进制读取
    loaded = pickle.load(f)
```

**注意：** pickle 文件是二进制的，不能用文本编辑器查看。

### 2.5 CSV 文件处理

```python
import csv

# 读取（字典方式，推荐）
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# 写入
with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])       # 写表头
    writer.writerows([["Alice", 18], ["Bob", 20]])  # 写多行
```

### 2.6 logging 模块

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("log.txt", encoding="utf-8"),
        logging.StreamHandler()    # 同时输出到控制台
    ]
)

logging.info("这是一条信息")     # 正常信息
logging.warning("这是一条警告")  # 警告信息
```

### 2.7 时间戳处理

```python
import time
import os.path

timestamp = os.path.getctime("file.txt")  # 获取创建时间的时间戳
readable = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
print(readable)  # 例如：2025-04-07 19:02:00
```

---

## 3. 常见错误

- **忘记 encoding**：读取中文文件时务必加 `encoding="utf-8"`
- **pickle 用文本模式**：必须是 `"wb"` 和 `"rb"`，不是 `"w"` 和 `"r"`
- **文件路径不存在**：写入前用 `os.path.exists()` 检查目录
- **CSV newline 参数**：写入 CSV 时要加 `newline=""`，否则会有空行
