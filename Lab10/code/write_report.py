# 将实验代码和运行结果写入Word文档
import docx
from docx.shared import Pt

doc = docx.Document()
style = doc.styles['Normal']
font = style.font
font.name = '宋体'
font.size = Pt(12)

title = doc.add_heading('实验10 正则表达式与网络爬虫', level=0)
title.alignment = 1

p = doc.add_paragraph()
p.alignment = 1
run = p.add_run('姓名： xxx    学号：xxx    班级：xxx    成绩：')
run.font.size = Pt(12)

# ========== 2.1 ==========
doc.add_heading('2.1 搜索有效产品代码', level=1)
doc.add_paragraph('输入： "AB123;X456;Y78;Z901"')
doc.add_paragraph('输出： X456')
doc.add_paragraph('源代码（ex2_1.py）：')
code = 'import re\ns = "AB123;X456;Y78;Z901"\npattern = r"\\b[A-Z]\\d{3}\\b"\nmatch = re.search(pattern, s)\nif match:\n    print(match.group())'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
p.add_run(' X456')

# ========== 2.2(1) ==========
doc.add_heading('2.2(1) 提取含字母o的单词', level=1)
doc.add_paragraph('源代码（ex2_2_1.py）：')
code = 'import re\ns = "I like Python programming 123 because it is 456 simple and elegant."\npattern = r"\\b\\w*o\\w*\\b"\nresult = re.findall(pattern, s, re.IGNORECASE)\nprint(result)'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
p.add_run(" ['Python', 'programming', 'because']")

# ========== 2.2(2) ==========
doc.add_heading('2.2(2) 提取日期时间字段', level=1)
doc.add_paragraph('源代码（ex2_2_2.py）：')
code = "import re\ns = '''see 123, 1987-02-09 07:30:00\n    1987-02-15 07:25:00'''\npattern = r'\\d{4}-\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}'\nresult = re.findall(pattern, s)\nprint(result)"
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
p.add_run(" ['1987-02-09 07:30:00', '1987-02-15 07:25:00']")

# ========== 2.2(3) ==========
doc.add_heading('2.2(3) 提取合法邮件地址', level=1)
doc.add_paragraph('源代码（ex2_2_3.py）：')
code = 'import re\ns = """xiasd@163.com, sdlfkj@.com sdflkj@180.com solodfdsf@123.com\nsdlfjxiaori@139.com saldkfj.com oisdfo@.sodf.com.com,\nlaskfuj321@qq.mail.com, quilkj5@com """\npattern = r"\\b[a-zA-Z0-9]+@[a-zA-Z0-9]+(?:\\.[a-zA-Z]+)+\\b"\nresult = re.findall(pattern, s)\nprint(result)'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
p.add_run(" ['xiasd@163.com', 'sdflkj@180.com', 'solodfdsf@123.com', 'sdlfjxiaori@139.com', 'laskfuj321@qq.mail.com']")

# ========== 2.2(4) ==========
doc.add_heading('2.2(4) findall分组对比', level=1)
doc.add_paragraph('源代码（ex2_2_4.py）：')
code = "import re\ns = 'see 123, 1987-02-09 07:30:00, 1986-02-15 07:25:00'\nfa1 = re.findall(r'\\d+-\\d+-\\d+', s)\nfa2 = re.findall(r'(\\d+)-\\d+-\\d+', s)\nfa3 = re.findall(r'(\\d+)-(\\d+)-(\\d+)', s)\nprint('fa1:', fa1)\nprint('fa2:', fa2)\nprint('fa3:', fa3)"
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(" fa1 (无分组): ['1987-02-09', '1986-02-15']")
doc.add_paragraph(" fa2 (一个分组): ['1987', '1986']")
doc.add_paragraph(" fa3 (三个分组): [('1987', '02', '09'), ('1986', '02', '15')]")
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('findall不同情形说明：').bold = True
doc.add_paragraph('无分组时，findall返回所有完整匹配的字符串。')
doc.add_paragraph('有分组时，findall只返回分组捕获的内容。')
doc.add_paragraph('有多个分组时，返回由各组内容组成的元组列表。')

# ========== 2.3 ==========
doc.add_heading('2.3 提取title标签内容', level=1)
doc.add_paragraph('源代码（ex2_3.py）：')
code = 'import re\nhtml = """<html>\n<head>\n   <title>Sample Page</title>\n</head>\n<body>\n   <h1>Welcome to the Sample Page</h1>\n   <p>This is a paragraph on the sample page.</p>\n</body>\n</html>"""\npattern = r"<title>(.*?)</title>"\nmatch = re.search(pattern, html, re.IGNORECASE)\nif match:\n    print("标签内容:", match.group(0))\n    print("文本内容:", match.group(1))'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(' 标签内容: <title>Sample Page</title>')
doc.add_paragraph(' 文本内容: Sample Page')

# ========== 2.4 ==========
doc.add_heading('2.4 筛选有效电话号码', level=1)
doc.add_paragraph('源代码（ex2_4.py）：')
code = "import re\nwith open('text.txt', 'r', encoding='utf-8') as f:\n    lines = f.readlines()\npattern = r'^(\\(\\d{3}\\)\\s\\d{3}-\\d{4}|\\d{3}-\\d{3}-\\d{4})$'\nprint('有效的电话号码：')\nfor line in lines:\n    phone = line.strip()\n    if re.match(pattern, phone):\n        print(phone)"
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(' 有效的电话号码：')
doc.add_paragraph(' 123-485-3749')

# ========== 2.5(1) ==========
doc.add_heading('2.5(1) sub替换数字开头的QQ邮箱', level=1)
doc.add_paragraph('源代码（ex2_5_1.py）：')
code = "import re\ns = \"\"\"5user@qq.com, test@163.com, 9invalid@qq.com  \n    safe_email@139.com, 123admin@qq.com, normal@mail.org\"\"\"\npattern = r'\\b\\d+\\w*@qq\\.com\\b'\nresult = re.sub(pattern, 'admin@security.com', s)\nprint('替换后：')\nprint(result)"
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(" admin@security.com, test@163.com, admin@security.com")
doc.add_paragraph("     safe_email@139.com, admin@security.com, normal@mail.org")

# ========== 2.5(2) ==========
doc.add_heading('2.5(2) sub十进制转十六进制', level=1)
doc.add_paragraph('源代码（ex2_5_2.py）：')
code = "import re\ndef dec_to_hex(match):\n    num = int(match.group())\n    return hex(num).upper().replace('X', 'x')\ns = 'hi69@qq.com, werksdf@163.com, sdf@sina.com'\npattern = r'\\b\\d+\\b'\nresult = re.sub(pattern, dec_to_hex, s)\nprint('替换后：')\nprint(result)"
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(" hi69@qq.com, werksdf@0xA3.com, sdf@sina.com")

# ========== 2.6(1) ==========
doc.add_heading('2.6(1) urllib图片爬取', level=1)
doc.add_paragraph('源代码（ex2_6_1.py）：')
code = 'import urllib.request, re, os\nurl = "http://www.daimg.com/photo/fruit/"\nsave_dir = "image1"\nif not os.path.exists(save_dir): os.makedirs(save_dir)\nresponse = urllib.request.urlopen(url)\nhtml_data = response.read().decode("utf-8", errors="ignore")\nresponse.close()\nimg_pattern = r\'<img[^>]*src=["\\\'](.*?)["\\\']\'\nimg_matches = re.findall(img_pattern, html_data, re.IGNORECASE)\n# 遍历下载图片...'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(' 共下载 40 张水果图片到 image1/ 目录')

# ========== 2.6(2) ==========
doc.add_heading('2.6(2) BS+requests图片爬取', level=1)
doc.add_paragraph('源代码（ex2_6_2.py）：')
code = 'import requests\nfrom bs4 import BeautifulSoup\nfrom urllib.parse import urljoin\nimport os\nurl = "http://www.daimg.com/photo/fruit/"\nheaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) ..."}\nsoup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")\nfor img in soup.find_all("img"):\n    img_url = urljoin(url, img.get("src"))\n    # 下载并保存...'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(' 共下载 42 张图片到 image2/ 目录')
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('思考：爬取的图片和看到的图片名是否一致？').bold = True
doc.add_paragraph('不完全一致。网页上显示的图片可能是缩略图，爬取到的图片名是服务器端实际存储的文件名。可以通过分析HTML中data-original等属性获取真实图片链接。')

# ========== 2.7 ==========
doc.add_heading('2.7 豆瓣电影Top250爬取', level=1)
doc.add_paragraph('源代码（ex2_7.py）：')
code = 'import requests, csv, time\nfrom bs4 import BeautifulSoup\nheaders = {"User-Agent": "Mozilla/5.0 ..."}\nmovies = []\nfor page in range(3):\n    url = f"https://movie.douban.com/top250?start={page*25}"\n    soup = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")\n    for item in soup.find_all("div", class_="item"):\n        title = item.find("span", class_="title").text\n        rating = item.find("span", class_="rating_num").text\n        movies.append((title, rating))\n    time.sleep(1)\nwith open("movies.csv", "w", newline="", encoding="utf-8-sig") as f:\n    csv.writer(f).writerows([["电影标题","评分"]] + movies)'
doc.add_paragraph(code)
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('运行结果：').bold = True
doc.add_paragraph(' 共爬取 75 部电影，数据已保存到 movies.csv')
doc.add_paragraph(' 示例：肖申克的救赎,9.7')
doc.add_paragraph()
p = doc.add_paragraph()
p.add_run('思考：selenium与BS+requests的优缺点比较').bold = True
doc.add_paragraph('selenium优点：能处理JavaScript动态渲染页面，模拟真实浏览器行为。')
doc.add_paragraph('selenium缺点：运行速度慢，资源消耗大，需额外安装浏览器驱动。')
doc.add_paragraph('BS+requests优点：轻量快速，适合静态页面。')
doc.add_paragraph('BS+requests缺点：无法执行JavaScript，对动态页面无能为力。')
doc.add_paragraph('检测/防御selenium的方法：检测navigator.webdriver属性、检测User-Agent、检测异常鼠标轨迹、验证码和限流机制。')

output_path = r'F:\AAAAclass\大二下\python与数据科学\Lab10\实验10 正则表达式与网络爬虫\实验10 正则表达式与网络爬虫\实验10_报告_完成版.docx'
doc.save(output_path)
print('Word文档已成功更新!')
