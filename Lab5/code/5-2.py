import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.01,4,1000)
y1=x**2
y2=np.log(x)
y3=1/(1+np.exp(-x))
plt.plot(x,y1,label='y=x^2')
plt.plot(x,y2,label='y=ln(x)')
plt.plot(x,y3,label='y=sigmoid')
plt.legend()
plt.show()
plt.show()