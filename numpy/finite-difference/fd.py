import numpy as np
x=np.arange(0,np.pi,0.1)


y=lambda x: np.sin(x)

dy=(y(x[2:])-y(x[0:-2]))/0.2

print(dy, np.cos(x))

print(dy-np.cos(x[1:-1]))


