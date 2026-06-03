# 习题2.6(1)：仅利用urllib模块完成图片爬取
# 目标网页：http://www.daimg.com/photo/fruit/

import urllib.request
import urllib.error
import re
import os

# 目标网址
url = "http://www.daimg.com/photo/fruit/"

# 创建保存图片的目录
save_dir = "Lab10/data/image1"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

try:
    # 获取网页源代码
    response = urllib.request.urlopen(url)
    html_data = response.read().decode('utf-8', errors='ignore')
    response.close()

    # 匹配图片链接：匹配<img>标签中的src属性
    img_pattern = r'<img[^>]*src=["\'](.*?)["\']'
    img_matches = re.findall(img_pattern, html_data, re.IGNORECASE)

    print(f"找到 {len(img_matches)} 个图片链接")

    count = 0
    for img_src in img_matches:
        # 处理相对路径
        if img_src.startswith('//'):
            img_url = 'http:' + img_src
        elif img_src.startswith('/'):
            img_url = url.rstrip('/') + img_src
        elif img_src.startswith('http'):
            img_url = img_src
        else:
            img_url = url + img_src

        try:
            # 下载图片
            img_data = urllib.request.urlopen(img_url, timeout=10).read()
            # 从URL中提取文件名
            img_name = img_url.split('/')[-1]
            if not img_name or '.' not in img_name:
                img_name = f"image_{count}.jpg"
            # 保存图片
            file_path = os.path.join(save_dir, img_name)
            with open(file_path, 'wb') as f:
                f.write(img_data)
            print(f"已下载: {img_name}")
            count += 1
        except Exception as e:
            print(f"下载失败: {img_url} - {e}")

    print(f"\n共下载 {count} 张图片到 {save_dir}/ 目录")

except Exception as e:
    print(f"网页访问失败: {e}")
