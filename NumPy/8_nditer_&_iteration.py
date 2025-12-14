import numpy as np

#iterating array-means going through the elements one by one

# 1-D
arr=np.array([1,2,4,5,6,7])
for i in arr:
    print(i)

# 2-D
arr=np.array([[1,2,4,5,6,7],[8,9,0,1,2,3]])
for i in arr:
    print(i)     #it will print in list not single elements.


# 2-D
arr=np.array([[1,2,4,5,6,7],[8,9,0,1,2,3]])
for i in arr:
    for j in i:
        print(j)     #it will print single elements.(also called nested looping)


print("iter function starts from here....")
#nditer function..
arr=np.array([[1,2,4,5,6,7],[8,9,0,1,2,3]])
for i in np.nditer(arr):
    print(i)


print("skipping elements........")
arr=np.array([[1,2,4,5,6,7],[8,9,0,1,2,3]])
for i in np.nditer(arr[: , ::2]):
    print(i)