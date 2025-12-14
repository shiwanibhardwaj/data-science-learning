#joining the numpy array-here we will pass concatenate()

import numpy as np
# arr1=np.array([1,2,3,4])
# arr2=np.array([5,6,7,8])
# arr=np.concatenate((arr1,arr2))
# print(arr)


#joining 2-d arrays along with rows(axis=1)
arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=np.array([[9,10,11,12],[13,14,15,16]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)

#joining array using stack function:

arr1=np.array([1,2,3,4])
arr2=np.array([9,10,11,12])
arr=np.stack((arr1,arr2),axis=1)
print(arr)

#hstack
arr1=np.array([1,2,3,4])
arr2=np.array([9,10,11,12])
arr=np.hstack((arr1,arr2))
print(arr)

#dstack
arr1=np.array([1,2,3,4])
arr2=np.array([9,10,11,12])
arr=np.dstack((arr1,arr2))
print(arr)

#vstack
arr1=np.array([1,2,3,4])
arr2=np.array([9,10,11,12])
arr=np.vstack((arr1,arr2))
print(arr)
