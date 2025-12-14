import numpy as np

a=np.array([1,2,3,4,5,6,4,7,8,4])
new_a=np.where(a==4) #it will return the array of indexes of values
print(new_a)

#searching even value ...
a=np.array([1,2,3,4,5,6,4,7,8,4])
new_a=np.where(a%2==0) #it will return the array of indexes of values
print(new_a)

#searching odd value ...
a=np.array([1,2,3,4,5,6,4,7,8,4])
new_a=np.where(a%2!=0) #it will return the array of indexes of values
print(new_a)

#searchsorted()-perform binary searching in array...
a=np.array([1,2,3,4,5,6,4,7,8,4])
new_a=np.searchsorted(a,8)  #it will sort and find the right index of value.
print(new_a)

a=np.array([1,2,3,4,5,6,4,7,8,4])
new_a=np.searchsorted(a,8,side='right') #it will sort and find right index of value but from right side. 
print(new_a)

#sort method()..
a=np.array([1,2,3,4,5,6,4,7,8,4])
print(np.sort(a)) 
print(a)#the real array remain unchanged.
 #on 2D-array..
a=np.array([[1,2,3,4,5],[6,4,7,8,4]])
print(np.sort(a))