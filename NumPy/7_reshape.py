import numpy as np
#Reshaping arrays..

#Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr=arr.reshape(4,3)
print(new_arr)

#Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_Arr=arr.reshape(2,2,3)
print(new_Arr)

#Unknown Dimension-(You are allowed to have one "unknown" dimension.

#Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

#Pass -1 as the value, and NumPy will calculate this number for you.)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_Arr=arr.reshape(2,2,-1)
print(new_Arr)
#Note: We can not pass -1 to more than one dimension.



#Flattening the arrays..
#Flattening array means converting a multidimensional array into a 1D array.
arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)