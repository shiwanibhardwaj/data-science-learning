import numpy as np
arr1=np.array([1,2,3,4,5,6])
arr2=np.array_split(arr1,4)
arr3=np.array_split(arr1,8)
print(arr2)
print(arr3)

#split into array with index...
arr1=np.array([1,2,3,4,5,6])
arr2=np.array_split(arr1,4)
print(arr2[0])
print(arr2[1])


a=np.array([[1,2,3],[6,7,8],[9,10,11],[12,13,14],[15,16,17]])
new_a=np.array_split(a,3,axis=1)
print(new_a)


#altarnate solution is using  the  hsplit()...
a=np.array([[1,2,3],[6,7,8],[9,10,11],[12,13,14],[15,16,17]])
new_a=np.hsplit(a,3)  #it will work same as array_split and we don't need to give axis in it as we give in array_split. 
print(new_a)