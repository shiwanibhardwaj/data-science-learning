import numpy as np
arr=np.array([1,2,3,4,5,7,8,9])
arr1=arr.reshape(2,4)
print(arr1)



arr2=np.array([1,2,3,4,5,7,8,9,1,2,3,4])
arr3=arr2.reshape(2,3,2)
print(arr3)