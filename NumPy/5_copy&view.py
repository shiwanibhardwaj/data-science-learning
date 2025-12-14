import numpy as np

# copy and view

a=np.array([1,2,3,4])
a1=a.copy()
a[0]=12
print(a)
print(a1)



a=np.array([1,2,3,4])
a1=a.view()

a[0]=12
print(a)
print(a1)

a1[0]=13
print(a)
print(a1)