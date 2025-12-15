import numpy as np
arr=np.array([1,2,3,4,5])
em_arr=[]
for i in arr:
    if i>2:
        em_arr.append(True)
    else:
        em_arr.append(False)

new_arr=arr[em_arr]
print(em_arr)
print(new_arr)


#filtering even values
arr=np.array([1,2,3,4,5])
em_arr=[]
for i in arr:
    if i%2==0:
        em_arr.append(True)
    else:
        em_arr.append(False)

new_arr=arr[em_arr]
print(em_arr)
print(new_arr)