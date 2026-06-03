import logging
import datetime
import os

logging.basicConfig(
    level=logging.INFO,  # 日志级别
    format="%(asctime)s - 用户名：%(message)s - 登录结果：%(levelname)s",  # 格式
    datefmt="%Y-%m-%d %H:%M:%S",  # 时间格式
    handlers=[
        logging.FileHandler("Lab3/output/login_log.txt", encoding="utf-8"),  # 写入日志文件
        logging.StreamHandler()  # 控制台输出
    ]
)

# 系统唯一合法用户
USER_NAME = "张三"
USER_PWD = "123456"

def login():
    input_name=input("请输入用户名：")
    input_pwd=input("请输入密码：")
    if input_name == USER_NAME and input_pwd == USER_PWD:
        logging.info(f"{input_name} - 登录成功")
        print("登录成功！")
    else:
        logging.warning(f"{input_name} - 登录失败")
        print("登录失败！")

def look_log():
    if os.path.exists("Lab3/output/login_log.txt"):
        with open("Lab3/output/login_log.txt", "r", encoding="utf-8") as f:
            for line in f:
                print(line.strip())
    else:
        print("日志文件不存在！")



if __name__ == "__main__":
    while True:
        sel = input("请输入你的操作：1——登录，2——查看日志，其他——退出\n")
        if sel == "1":
            login()
        elif sel == "2":
            look_log()
        else:
            print("退出系统！")
            break;
