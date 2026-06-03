import random
import os

def fs(dirname,s):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    files=[f for f in os.listdir(dirname) if f.endswith(".txt")]
    if not files:
        path=os.path.join(dirname,"new.txt")
        with open(path,"a",encoding = "utf-8") as f:
            f.write(s+"\n")
        return
    target=random.choice(files)
    path=os.path.join(dirname,target)
    with open(path,"a",encoding="utf-8") as f:
        f.write(s+"\n")

if __name__ == "__main__":
    fs("test_dir", "这是要保存的内容")
    