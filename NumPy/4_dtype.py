import numpy as np

#data types in numpy...

"""
i for int 
f for float
c for complex float
b for boolean
u for unsigned int
m for timedelta
U for unicode string
S for string
M for datetime
V for memory junk
O for object
"""

arr=np.array([1,2,3,4])
print(arr.dtype)


string=np.array(['shivani','kumai'])
print(string.dtype)

# creating an array with defined data type

ar=np.array([1,2,3,4],dtype='S')
print(ar)
print(ar.dtype)
#creating an array with data type of 4 byte int....

arr1=np.array([1,2,3,4],dtype='S4')
print(arr1.dtype)
print(arr1)

#converting data type in existing array-astype()

sh=np.array([1.1,2.1,3.1])
new_sh=sh.astype(int)
print(new_sh)
print(new_sh.dtype)