# 习题2.5(1)：将以数字开头的QQ邮箱替换为 admin@security.com

import re

s = """5user@qq.com, test@163.com, 9invalid@qq.com  
    safe_email@139.com, 123admin@qq.com, normal@mail.org"""

# 匹配以数字开头的qq邮箱：数字开头 + 任意字符 + @qq.com
pattern = r'\b\d+\w*@qq\.com\b'

# 替换为admin@security.com
result = re.sub(pattern, 'admin@security.com', s)

print("替换前：")
print(s)
print("\n替换后：")
print(result)
