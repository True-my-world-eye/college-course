import random
import time
import datetime
import math

print(f"(a)当前时间戳：{time.time()}")
print(f"(b)当前日期：{datetime.datetime.today()}")
print(f"(c)当前时间字符串：{str(datetime.datetime.now())}")

#生成1000个1-10之间的随机数
nums=[random.randint(1,10)for i in range(1000)]
#平均值
avg=sum(nums)/len(nums);
#标准差
var=sum((x-avg)**2 for x in nums)/len(nums)
std=math.sqrt(var)

#频率字典
freq = {i:nums.count(i) for i in range(11)}

print("(d) 平均值:", avg)
print("标准差:", std)
print("各数字出现次数:", freq)