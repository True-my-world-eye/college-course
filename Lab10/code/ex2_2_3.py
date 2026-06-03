# 习题2.2(3)：找出文本中全体合法的邮件地址

import re

s = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com sdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com, laskfuj321@qq.mail.com, quilkj5@com """

# 合法邮箱：用户名由字母数字组成，@后域名包含点，域名最后是常见顶级域
pattern = r'\b[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\.[a-zA-Z]+)+\b'
result = re.findall(pattern, s)

print(result)
# 输出：['xiasd@163.com', 'sdflkj@180.com', 'solodfdsf@123.com', 'sdlfjxiaori@139.com', 'laskfuj321@qq.mail.com']
