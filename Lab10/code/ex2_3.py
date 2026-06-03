# 习题2.3：使用正则表达式找到<title>标签并提取内容

import re

html = """<html>
<head>
   <title>Sample Page</title>
</head>
<body>
   <h1>Welcome to the Sample Page</h1>
   <p>This is a paragraph on the sample page.</p>
</body>
</html>"""

# 使用search定位<title>标签，并用分组提取标签内文本
pattern = r'<title>(.*?)</title>'
match = re.search(pattern, html, re.IGNORECASE)

if match:
    print("标签内容:", match.group(0))
    print("文本内容:", match.group(1)) 
