# Lab1 Python 入门练习 — 知识文档

## 1. 实验目标概览
- 了解 Python 的多种运行方式
- 掌握基本数据结构（字符串、列表、字典、集合、元组）
- 学会使用条件判断（if/else）和循环（for）
- 熟悉 `print()` 函数和格式化输出

---

## 2. 核心知识点

### 2.1 Python 的四种运行方式

| 方式 | 说明 | 适用场景 |
|------|------|---------|
| 交互式 (cmd 输入 `python`) | 逐行输入代码，立即看到结果 | 快速测试小段代码 |
| IDE (PyCharm/Spyder) | 完整开发环境 | 开发大型项目 |
| Jupyter Notebook | 网页版，代码/结果/图文混排 | 数据分析和教学 |
| 命令行执行 `python xxx.py` | 运行完整的 .py 文件 | 正式运行程序 |

### 2.2 字符串操作

```python
s = "hello123"
s.isalpha()   # 是否全是字母 → False（因为有数字）
s.isdigit()   # 是否全是数字 → False
"123".isdigit()  # True
```

**重要方法：**
- `len(s)` — 字符串长度
- `s.count(sub)` — 子串出现次数
- `s.split(sep)` — 按分隔符拆分
- `s.upper()` / `s.lower()` — 大小写转换

### 2.3 格式化输出（f-string）

```python
name = "Alice"
score = 85
print(f"{name}: {score}")           # 直接嵌入变量
print(f"{score:.2f}")               # 保留2位小数
print(f"{'hello':>10}")             # 右对齐，占10个字符宽度
```

### 2.4 字典基础

```python
# 创建字典
student_scores = {"Alice": 85, "Bob": 90}

# 遍历
for name, score in student_scores.items():
    print(name, score)

# 获取最大值对应的键
max_student = max(student_scores, key=student_scores.get)
# key=... 指定比较规则：按字典的值来比较
```

### 2.5 列表合并

```python
list1 = [1, 2, 3]
list2 = [100, 200, 300]
merged = list1 + list2  # [1, 2, 3, 100, 200, 300]
```

### 2.6 for 循环与 range

```python
# range(1, 101) → 1 到 100
for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print(i)  # 既能被2整除又能被3整除
```

### 2.7 导入模块

```python
import math
import time
import datetime

math.pow(3, 2)     # 3的2次方，返回浮点数
math.log(2, 10)    # 以10为底的log2
time.time()        # 当前时间戳
datetime.datetime.now()  # 当前日期时间
```

---

## 3. 初学者常见错误

- **忘记冒号**：`if x > 10:` 后面的 `:` 不能丢
- **缩进不一致**：Python 用缩进表示代码块，混用空格和 Tab 会报错
- **字典键写错**：`student_scores.get("alice")` 和 `"Alice"` 不同（大小写敏感）
- **range 的结束值**：`range(1, 101)` 包含 1 但不包含 101
