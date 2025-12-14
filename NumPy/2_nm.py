#now we will create a numpy ndarray obj(the array obj in numpy called ndarray).

import numpy as np
x=np.array([1,2,3,4,5])
print(type(x))
print(x)

#array with tuple
y=np.array((1,2,3,4))
print(y)
print(type(y))

#multi dimensional array
a=np.array([[1,2,4,6],[7,8,9,0],[7,8,9,2]])
print(a)

a1=np.array([[[1,2,4,6],[7,8,9,0],[7,8,9,2]]])
print(a1)
print(f"dimensions of a1:{a1.ndim}")

a2=np.array([1,24,6,5],ndmin=4)
print(a2)

#array attributes..
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)


#spacial arrays....
print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.eye(5))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))
print(np.full((2, 2), 7))



arr=np.arange(50).reshape(5,10)
print(arr)


#operations on the same array..
print(f'addition of arr with itself:\n {arr+arr}')
print(f'subtraction of arr with itself:\n {arr-arr}')
print(f'multiplication of arr with itself:\n {arr*arr}')


#Broadcasting.....
arr = np.array([1, 2, 3])
print(arr + 5)