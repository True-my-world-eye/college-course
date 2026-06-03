import os
file_name="Lab3/data/oldfilename.txt"
if os.path.exists(file_name):
    with open(file_name,"r") as f:
        content=f.read()
        print(content)
else:
    # 不存在则创建文件
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("初始创建内容")  # 写入默认内容
    print(f"文件{file_name}不存在，已自动创建")