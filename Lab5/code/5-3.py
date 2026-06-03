import numpy as np

arr=np.random.randn(9,10)

print("(a)\n",arr[1,4],arr[5,2])
print("(b)\n",arr[2:5,3:6])
print("(c)\n",arr[2:5,[0,1,3]])


arr[arr>1]=10.00
arr[arr<-1]=-10.00
print("(d)\n",arr)