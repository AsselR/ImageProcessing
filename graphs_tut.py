import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2, 2, 100)
y=-2*x+4

y1=2*(x**2)

y2=3*(x**3)

y3=-(x**2)+3

y4=(x**2)-4*x+7

x1 = np.arange(0,4*np.pi,0.1)
y5=np.cos(x1)

y6=np.sin(x1)

fig, (ax)=plt.subplots(2, 3)

ax[0,0].plot(x,y)
ax[0,0].set_title('y=-2*x+4')

ax[0, 1].plot(x, y1)
ax[0,1].set_title('y1=2*(x**2)')

ax[0,2].plot(x, y2)
ax[0,2].set_title('y2=3*(x**3)')

ax[1,0].plot(x, y3)
ax[1, 0].set_title('y3=-(x**2)+3')

ax[1, 1].plot(x, y4)
ax[1,1].set_title('y4=(x**2)-4*x+7')
ax[1,2].plot(x1, y5)
ax[1, 2].plot(x1, y6)
plt.legend(['cosx', 'sinx'])

plt.show()