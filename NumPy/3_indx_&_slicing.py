#numpy array indexing and slicing 

import numpy as np
#1-D
arr1=np.array([1,2,3,4])
print(arr1[0])

#2-D
arr2=np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr2[1 , 2])

#3-D

arr3=np.array([[[1,2,3,4,5],[6,7,8,9,0],[16,17,18,19,10]]])
print(arr3[0, 2 , 2])



#Boolean Indexing.....
a = np.array([5, 10, 15, 20, 25])
print(a[a > 15])
print(a[(a > 10) & (a < 25)])

#numpy array slicing 

print(arr1[1:3])
print(arr1[-3:-1])

print(arr2[1,1:4])
print(arr2[0,1:4])
print(arr2[0:2,3])
print(arr2[0:2,1:4])


#ex of slicing...
arr=np.array([[[1,2,3,4],[5,6,7,8],[7,8,9,10]],[[1,2,3,4],[5,12,7,8],[7,8,9,10]]])
print(arr[1,1,1])
print(arr[0,:2,:3])

#conditional slicing ....
arr=np.arange(1,10)
value=arr>5  # returns boolean 
print(value)
print(arr[value])


