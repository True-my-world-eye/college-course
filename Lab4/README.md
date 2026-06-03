# Lab4 模块与面向对象编程 — 知识文档

## 1. 实验目标概览
- 理解模块（module）和包（package）的概念
- 掌握类的定义、继承、封装
- 学会使用 `__init__.py` 创建包
- 熟悉 `if __name__ == "__main__"` 的用法

---

## 2. 核心知识点

### 2.1 模块（Module）

一个 `.py` 文件就是一个模块。

```python
# 导入模块的几种方式
import math                    # 用 math.pow(3, 2)
import math as m               # 用 m.pow(3, 2)
from math import pow           # 直接用 pow(3, 2)
from math import *             # 导入所有（不推荐，可能命名冲突）
```

**`if __name__ == "__main__"` 的作用：**

```python
# mc.py
class Student:
    ...

if __name__ == "__main__":
    # 这部分代码只在直接运行 mc.py 时执行
    # 当被 import 时不会执行
    s = Student("Alice", 18)
```

这可以用来区分"当前文件是作为主程序运行"还是"被其他地方导入作为模块使用"。

### 2.2 包（Package）

包就是一个包含 `__init__.py` 的文件夹。

```
mypack/
├── __init__.py    # 包的初始化文件（可以为空）
├── aa.py          # 模块
└── subpack/       # 子包
    ├── __init__.py
    └── bb.py
```

```python
# 导入包中的模块
from mypack.aa import add
from mypack.subpack.bb import sub
from mypack import a, b  # __init__.py 中定义的变量
```

### 2.3 类（Class）与面向对象

```python
class Person:
    def __init__(self, name, age):
        self.name = name      # 公开属性
        self.__age = age      # 私有属性（两个下划线开头）
    
    def get_info(self):
        return self.name, self.__age
```

**重要概念：**
- `__init__`：构造函数，创建对象时自动调用
- `self`：代表当前实例，必须作为第一个参数
- `__name`：私有属性（name mangling），外部不能直接访问
- `get_info()`：方法，可以访问私有属性

### 2.4 继承（Inheritance）

```python
class Student(Person):          # 继承 Person
    def __init__(self, name, age, scores):
        super().__init__(name, age)  # 调用父类的构造函数
        self.scores = scores
    
    def avg(self):
        return sum(self.scores) / len(self.scores)
    
    def get_info(self):
        info = super().get_info()    # 调用父类方法
        return info, self.scores
```

**`super()` 的作用**：调用父类的方法，避免重复写父类的代码。

### 2.5 常用内置模块

| 模块 | 常用函数 |
|------|---------|
| `random` | `randint(a,b)`, `random()`, `choice()`, `shuffle()` |
| `time` | `time()`, `sleep(sec)`, `localtime()` |
| `datetime` | `datetime.now()`, `date.today()`, `timedelta()` |
| `hashlib` | `md5(b).hexdigest()` |
| `zipfile` | `ZipFile()`, `extractall()` |
| `os` | `listdir()`, `mkdir()`, `remove()` |

---

## 3. 常见错误

- **忘记 self**：类方法第一个参数必须是 `self`
- **私有属性访问**：`obj.__name` 会报错，应通过方法访问
- **`__init__.py` 缺失**：Python 3.3+ 虽然不强制，但创建包时建议加上
- **继承时未调用 super()**：父类的 `__init__` 不会自动执行
