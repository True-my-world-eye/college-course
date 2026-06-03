# 习题2.5(2)：将文本中的十进制数字转为十六进制

import re

s = "hi69@qq.com, werksdf@163.com, sdf@sina.com"

# 替换函数：将匹配到的十进制数字转为十六进制
def dec_to_hex(match):
    num = int(match.group())
    return hex(num).upper().replace('X', 'x')

# 匹配数字（但排除邮箱@后面的数字部分）
pattern = r'\b\d+\b'
result = re.sub(pattern, dec_to_hex, s)

print("替换前：")
print(s)
print("\n替换后：")
print(result)
