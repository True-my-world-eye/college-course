import os
import shutil
import pickle
def wordcount(w,txtfile):
    """
    统计关键字出现次数
    :param w: 要统计的关键字（字符串）
    :param txtfile: 文本文件路径（字符串）
    :return: 关键字出现次数（整数）
    """
    try:
        with open(txtfile, 'r', encoding='utf-8') as f:
            text = f.read()
            count = text.count(w)
            return count
    except FileNotFoundError:
        return 0

if not os.path.exists("Lab3/mydir"):
    os.mkdir("Lab3/mydir")
    print("已创建目录：Lab3/mydir")
else:
    print("目录已存在：Lab3/mydir")

news_files=[f for f in os.listdir("Lab3/data") if f.startswith("news_") and f.endswith(".txt")]

for file in news_files:
    src_path = os.path.join("Lab3/data", file)
    dst_path = os.path.join("Lab3/mydir", file)
    print(f"src_path:{src_path}")
    print(f"dst_path:{dst_path}")
    shutil.copy2(src_path, dst_path)

save_data = [wordcount, news_files]
pkl_path = os.path.join("Lab3/mydir", "wc.pkl")
with open(pkl_path, "wb") as f:  # pickle需二进制写入wb
    pickle.dump(save_data, f)
print("数据已保存至Lab3/mydir/wc.pkl")

with open(pkl_path, "rb") as f:  # 二进制读取rb
    load_func, load_files = pickle.load(f)

keywords = ["中国", "美国", "科技", "芯片"]
# 遍历关键字和文件，统计次数
for kw in keywords:
    total = 0
    for file in load_files:
        file_path = os.path.join("Lab3/mydir", file)
        total += wordcount(kw, file_path)
    print(f"关键字【{kw}】在所有文件中出现的总次数：{total}")