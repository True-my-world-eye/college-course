import numpy as np

arr=np.random.uniform(10,20,(10,5))
print("arr:\n",arr)

# (a) 每行减均值
row_mean = arr.mean(axis=1, keepdims=True)
new_arr = arr - row_mean
print("(a)\n", new_arr)

# (b) 保存 csv，3位小数，逗号分隔
np.savetxt("Lab5/output/dat.csv", new_arr, delimiter=",", fmt="%.3f")

# (c) 读取并交换第1、2行
load_arr = np.loadtxt("Lab5/output/dat.csv", delimiter=",")
load_arr[[0,1]] = load_arr[[1,0]]
print("(c)\n", load_arr)

# (d) 按第2列从小到大排序
sorted_arr = load_arr[load_arr[:,1].argsort()]
print("(d)\n", sorted_arr)