import numpy as np
a=np.array([[1,2,3],[6,7,8],[9,10,11],[12,13,14],[15,16,17]])
new_a=np.array_split(a,3,axis=1)
print(new_a)
