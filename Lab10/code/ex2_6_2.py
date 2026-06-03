# 习题2.6(2)：使用Beautiful Soup和requests完成图片爬取
# 目标网页：http://www.daimg.com/photo/fruit/

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

# 目标网址
url = "http://www.daimg.com/photo/fruit/"

# 请求头，模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 创建保存图片的目录
save_dir = "Lab10/data/image2"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

try:
    # 获取网页源代码
    resp = requests.get(url=url, headers=headers, timeout=10)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')

    # 找到所有img标签
    img_tags = soup.find_all('img')
    print(f"找到 {len(img_tags)} 个图片标签")

    count = 0
    for img in img_tags:
        # 获取src属性
        src = img.get('src')
        if not src:
            continue

        # 处理相对路径，转为完整URL
        img_url = urljoin(url, src)

        try:
            # 下载图片
            img_resp = requests.get(img_url, headers=headers, timeout=10)
            img_data = img_resp.content

            # 从URL中提取图片文件名
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
    resp.close()

except Exception as e:
    print(f"网页访问失败: {e}")
