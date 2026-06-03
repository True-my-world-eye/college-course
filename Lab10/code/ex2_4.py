# 习题2.4：从text.txt中输出所有有效电话号码
# 有效格式：(xxx) xxx-xxxx 或 xxx-xxx-xxxx

import re

# 读取text.txt文件
with open('Lab10/data/text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 匹配两种格式的电话号码
pattern = r'^(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$'

print("有效的电话号码：")
for line in lines:
    phone = line.strip()
    if re.match(pattern, phone):
        print(phone)
