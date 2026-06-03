# 习题2.2(2)：提取每行中完整的年月日和时间字段

import re

s = '''see 123, 1987-02-09 07:30:00
    1987-02-15 07:25:00'''

# 匹配完整的日期时间格式：YYYY-MM-DD HH:MM:SS
pattern = r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}'
result = re.findall(pattern, s)

print(result)  
