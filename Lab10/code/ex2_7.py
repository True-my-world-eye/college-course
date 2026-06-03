# 习题2.7：爬取豆瓣电影Top250前3页，提取标题和评分，保存到movies.csv

import requests
from bs4 import BeautifulSoup
import csv
import time

# 请求头，模拟浏览器访问，避免触发反爬机制
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

# 存储所有电影数据
movies = []

# 爬取前3页，每页25条，start参数控制分页
for page in range(3):
    start = page * 25
    url = f"https://movie.douban.com/top250?start={start}"

    try:
        resp = requests.get(url=url, headers=headers, timeout=10)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')

        # 每部电影在class为item的div中
        items = soup.find_all('div', class_='item')
        for item in items:
            # 获取电影标题
            title_tag = item.find('span', class_='title')
            if title_tag:
                title = title_tag.text
            else:
                continue

            # 获取评分
            rating_tag = item.find('span', class_='rating_num')
            if rating_tag:
                rating = rating_tag.text
            else:
                continue

            movies.append((title, rating))
            print(f"第{page+1}页 - {title}: {rating}")

        # 礼貌性延迟，避免请求过快
        time.sleep(1)

    except Exception as e:
        print(f"第{page+1}页爬取失败: {e}")

# 保存到movies.csv
with open('Lab10/data/movies.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerow(['电影标题', '评分'])
    writer.writerows(movies)

print(f"\n共爬取 {len(movies)} 部电影，数据已保存到 movies.csv")
