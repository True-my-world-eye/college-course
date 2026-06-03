# Lab10 正则表达式与网络爬虫 — 知识文档

## 1. 实验目标概览
- 掌握正则表达式的基本语法和常见模式
- 学会用 `re` 模块进行文本搜索、匹配和替换
- 理解 HTTP 请求和网页爬取的基本原理
- 学会用 `requests` + `BeautifulSoup` 爬取静态网页
- 了解 `urllib` 模块的使用

---

## 2. 核心知识点

### 2.1 正则表达式入门

正则表达式是一种**模式匹配语言**，用来在文本中查找符合特定规则的字符串。

#### 常用元字符

| 符号 | 含义 | 示例 |
|------|------|------|
| `.` | 匹配任意单个字符 | `a.b` 匹配 "acb"、"a b" |
| `\d` | 匹配数字 (0-9) | `\d{3}` 匹配三位数 |
| `\w` | 匹配字母、数字、下划线 | `\w+` 匹配一个单词 |
| `\s` | 匹配空格、制表符、换行 | |
| `*` | 前一个字符出现 0 次或多次 | `ab*c` 匹配 "ac"、"abc"、"abbc" |
| `+` | 前一个字符出现 1 次或多次 | `ab+c` 匹配 "abc"、"abbc" |
| `?` | 前一个字符出现 0 次或 1 次 | `colou?r` 匹配 "color"、"colour" |
| `{n}` | 重复 n 次 | `\d{4}` 匹配 4 位数字 |
| `{n,m}` | 重复 n 到 m 次 | `\d{2,4}` |
| `^` | 字符串开头 | `^Hello` 匹配以 Hello 开头的字符串 |
| `$` | 字符串结尾 | `end$` 匹配以 end 结尾的字符串 |
| `[]` | 字符集合 | `[aeiou]` 匹配任意元音字母 |
| `()` | 分组 | `(ab)+` 匹配 "ab"、"abab" |

#### 常见模式举例

```python
import re

# 匹配邮箱
pattern = r"\b[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\.[a-zA-Z]+)+\b"
re.findall(pattern, "abc@163.com, xyz@gmail.com")

# 匹配电话号码 (xxx) xxx-xxxx 或 xxx-xxx-xxxx
pattern = r"^(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"

# 匹配日期时间 2025-04-07 07:30:00
pattern = r"\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}"

# 提取 HTML 标签内容
pattern = r"<title>(.*?)</title>"
# .*? 中的 ? 表示非贪婪匹配：匹配尽可能短的字符串
```

### 2.2 re 模块核心函数

```python
import re

re.search(pattern, string)     # 搜索第一个匹配，返回 Match 对象
re.match(pattern, string)      # 从字符串开头匹配
re.findall(pattern, string)    # 找出所有匹配，返回列表
re.sub(pattern, repl, string)  # 替换匹配的内容
re.split(pattern, string)      # 按匹配分割
```

**findall 的重要细节：**

```python
# 无分组：返回所有完整匹配
re.findall(r"\d+-\d+-\d+", s)        # ['1987-02-09', '1986-02-15']

# 有分组：只返回分组内容
re.findall(r"(\d+)-\d+-\d+", s)      # ['1987', '1986']

# 多分组：返回元组列表
re.findall(r"(\d+)-(\d+)-(\d+)", s)  # [('1987','02','09'), ('1986','02','15')]
```

### 2.3 re.sub 替换

```python
# 简单替换
result = re.sub(r"\b\d+@qq\.com\b", "admin@security.com", text)

# 函数替换（强大！）
def dec_to_hex(match):
    num = int(match.group())   # match.group() 拿到匹配的字符串
    return hex(num)

result = re.sub(r"\b\d+\b", dec_to_hex, text)
```

### 2.4 requests + BeautifulSoup 爬虫

```python
import requests
from bs4 import BeautifulSoup

# 1. 发送请求，获取网页
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; ...)"
}
resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")

# 2. 提取信息
# 按标签查找
titles = soup.find_all("span", class_="title")

# 按 CSS 选择器
items = soup.select("div.item")

# 3. 提取属性或文本
for item in items:
    title = item.find("span", class_="title").text
    link = item.find("a")["href"]
```

### 2.5 urllib（Python 内置）

```python
import urllib.request

response = urllib.request.urlopen(url)
html = response.read().decode("utf-8", errors="ignore")
response.close()
```

### 2.6 爬虫礼仪

```python
import time
time.sleep(1)  # 每请求一页休息1秒，避免被封 IP
```

---

## 3. 初学者常见问题

- **反爬虫**：很多网站会检测 User-Agent，记得伪装成浏览器
- **编码问题**：`.encoding = "utf-8"` 或 `.decode("utf-8", errors="ignore")`
- **动态页面**：BS+requests 只能处理静态页面，动态页面需要 Selenium
- **正则贪婪匹配**：`.*` 会匹配尽可能多，`.*?` 匹配尽可能少
- **分组和非贪婪**：两者不同，`(.*?)` 是分组 + 非贪婪
- **相对路径转绝对**：用 `urljoin(base_url, relative_path)` 
