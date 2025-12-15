import numpy as np
from numpy import random
arr=random.randint(100)
print(arr)

#can also generate float() via rand() from 0 to 1.
arr=random.rand()
print(arr)

#can also generate random array....
arr=random.randint(100,size=(3,6))
print(arr)

#choice()...
arr=random.choice([1,2,3,4,5,8,7],size=(3,5))
print(arr)