import numpy as np
import time

mat=np.random.randn(1000,1000)

#numpy版本
start =time.time()
min_val=mat.min()
max_val=mat.max()
mat_norm=(mat-min_val)/(max_val-min_val)
print("numpy version time:",time.time()-start)
print("max/min",mat_norm.max(),mat_norm.min())

#纯python版本
start = time.time()
lst = mat.tolist()
minv = min(min(row) for row in lst)
maxv = max(max(row) for row in lst)
for i in range(1000):
    for j in range(1000):
        lst[i][j] = (lst[i][j]-minv)/(maxv-minv)
print("Python version time:", time.time()-start)