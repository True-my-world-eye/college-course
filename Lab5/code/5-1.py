from scipy.optimize import minimize
import numpy as np

def func(x):
    return (x-2)**2+3

res=minimize(func,x0=0)
print("最小值点 x =", res.x[0])
print("最小函数值 =", res.fun)