import numpy as np
A=np.random.uniform(0,1,20000)
B=np.random.normal(3,2,20000)
C=np.random.randn(20000)

# (a) A+C
print("(a)\n",A+C)

# (b) A/B
print("(b)\n",A/B)

# (c) 逐元素乘积
print("(c)\n",A*B)

# (d) 内积+对数
D = abs(np.dot(A, B))
E = abs(np.dot(B, C))
print("(d)\n", np.log(E+2) + np.log(D+2))

# (e) 中位数、标准差、四分位数
print("中位数", np.median(B))
print("标准差", np.std(B))
print("Q1/Q3", np.percentile(B, [25,75]))