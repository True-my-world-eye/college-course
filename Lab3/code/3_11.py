import csv


temp_list = []  # 温度列表，用于计算平均值
humidity_list = []  # 湿度列表，用于找最大值
light_sum = 0  # 光照强度总和
abnormal_data = []  # 温度超过30℃的异常数据

with open("Lab3/data/exp_data.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.DictReader(f)  # 按列名读取
    for row in csv_reader:
        # 转换数据类型（字符串→数值）
        date = row["date"]
        temp = float(row["temperature"])
        humidity = float(row["humidity"])
        light = float(row["light"])
        # 追加到对应列表
        temp_list.append(temp)
        humidity_list.append(humidity)
        light_sum += light
        # 筛选异常数据（温度>30）
        if temp > 30:
            abnormal_data.append((date, temp, humidity, light))

# 计算统计指标
avg_temp = round(sum(temp_list) / len(temp_list), 2) if temp_list else 0.0
max_humidity = max(humidity_list) if humidity_list else 0.0

# 将统计结果写入report.txt
with open("Lab3/data/report.txt", "w", encoding="utf-8") as f:
    # 写入基本统计
    f.write("===== 实验数据统计报告 =====\n")
    f.write(f"平均温度：{avg_temp}℃\n")
    f.write(f"最高湿度：{max_humidity}\n")
    f.write(f"光照强度总和：{light_sum}\n")
    # 写入异常数据
    f.write(f"\n===== 温度超过30℃的异常数据 =====\n")
    f.write("日期\t\t温度\t湿度\t光照强度\n")
    for data in abnormal_data:
        f.write(f"{data[0]}\t{data[1]:.1f}\t{data[2]:.1f}\t{data[3]:.1f}\n")

print("数据统计完成，报告已保存至Lab3/data/report.txt")
print(f"平均温度：{avg_temp}℃，最高湿度：{max_humidity}，光照总和：{light_sum}")
print(f"温度超过30℃的异常数据共{len(abnormal_data)}条")