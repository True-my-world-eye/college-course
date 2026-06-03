# Lab2 Python 基础语法实践 — 知识文档

## 1. 实验目标概览
- 掌握函数的定义和调用
- 掌握 lambda 表达式（匿名函数）
- 学会使用 `map()`、`filter()`、`reduce()` 和 `sorted()`
- 理解列表推导式

---

## 2. 核心知识点

### 2.1 函数的定义

```python
def count(s):
    upper = lower = digit = other = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digit += 1
        else:
            other += 1
    return (upper, lower, digit, other)
```

**要点：**
- `def` 关键字定义函数
- `return` 返回结果（可以是元组）
- 参数不需要声明类型（但可以用 `: type` 做注解）

### 2.2 Lambda 表达式（匿名函数）

```python
# 普通函数
def add(x, y):
    return x + y

# 等价 lambda
add_lambda = lambda x, y: x + y

# 最常用场景：sorted 的 key 参数
sorted(stock_list, key=lambda x: x["price"])
```

### 2.3 sorted() 多级排序

```python
# 先按总价降序（-变负号），总价相同时按单价降序
sorted(stock_list, key=lambda x: (-x["total"], -x["price"]))

# 按成绩降序，成绩相同按年龄升序
sorted(students, key=lambda x: (-x["score"], x["age"]))
```

**技巧：** 想让排序"从小到大"就不用管，想"从大到小"要么加 `reverse=True`，要么在数字前加 **负号**。

### 2.4 map / filter / reduce

| 函数 | 作用 | 返回 |
|------|------|------|
| `map(f, list)` | 对每个元素应用函数 f | 迭代器 |
| `filter(f, list)` | 筛选出使 f 为 True 的元素 | 迭代器 |
| `reduce(f, list)` | 累积计算（需 `from functools import reduce`）| 单个值 |

**示例：**

```python
from functools import reduce

products = [{"price": 10.5}, {"price": 5.2}, {"price": 7.8}]

# map: 提取所有价格
prices = list(map(lambda x: x["price"], products))

# reduce: 求总和
total = reduce(lambda x, y: x + y, prices)

# filter: 筛选价格高于平均的商品
avg = total / len(prices)
high = list(filter(lambda x: x["price"] > avg, products))
```

### 2.5 质因子分解

```python
def prime_factors(n):
    factors = []
    count = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            cnt = 0
            while n % d == 0:
                n //= d
                cnt += 1
            factors.append(d)
            count.append(cnt)
        d += 1
    if n > 1:
        factors.append(n)
        count.append(1)
    return [factors, count]
```

### 2.6 罗马数字转换

```python
# 关键思路：从左到右遍历，如果当前 < 下一个则减，否则加
def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50,
              "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
            total -= values[s[i]]
        else:
            total += values[s[i]]
    return total
```

---

## 3. 常见错误

- **lambda 写法**：`lambda x, y: x + y` 没有 `return`
- **map/filter 返回迭代器**：需要用 `list()` 才能打印
- **reduce 需导入**：不要忘记 `from functools import reduce`
- **sorted 不改变原列表**：它返回新列表，原数据不变
