import shutil
import os.path
import time

with open("Lab3/data/original_file.txt","w") as f:
    f.write("Hello world")

shutil.copyfile("Lab3/data/original_file.txt", "Lab3/data/copy_file.txt")
# 获取复制文件的创建时间
create_time = os.path.getctime("Lab3/data/copy_file.txt")
# 时间戳转成可读格式
format_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(create_time))
print(f"复制文件的创建时间: {format_time}")