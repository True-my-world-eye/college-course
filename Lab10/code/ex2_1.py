# 习题2.1：使用search函数找到第一个有效产品代码，并使用group函数打印结果
# 有效的产品代码：以大写字母开头，紧随其后恰好3位数字，整个代码长度为4个字符

import re

s = "AB123;X456;Y78;Z901"

# 正则表达式：大写字母开头 + 恰好3位数字，整体4个字符
# 注意要用\b表示单词边界，确保匹配独立的4字符代码
pattern = r'\b[A-Z]\d{3}\b'

# 使用search查找第一个匹配项
match = re.search(pattern, s)

if match:
    print(match.group())  
