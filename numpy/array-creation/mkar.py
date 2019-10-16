import numpy as np
ar =[1,2, 3.4]
print(type(ar))
ar = np.array(ar)
print(type(ar))

ar=np.arange(-2,2.01,0.2)
print(ar)


ar = np.arange(0.5,1.6,0.1)
ar = np.linspace(0.5,1.5,11)
print(ar)
print(ar[0:-1:2])



ass= 'acvfgkdjbdblknlkrnb'
a = np.array(( list(ass)), dtype='c')
print(a,type(a))
   
