import numpy as np
import matplotlib.pyplot as plt  

data = np.random.normal(-1,1,10000)
plt.hist(data,bins=100)
plt.title("N(-1,1)分布直方图")
plt.xlabel("x")
plt.ylabel("频数")
plt.show()