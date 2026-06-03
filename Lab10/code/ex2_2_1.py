# 习题2.2(1)：提取字符串中含字母'o'的全部单词

import re

s = "I like Python programming 123 because it is 456 simple and elegant."

# 提取含字母o的单词：\b\w*o\w*\b 匹配包含o的完整单词
pattern = r'\b\w*o\w*\b'
result = re.findall(pattern, s, re.IGNORECASE)

print(result)  
