import pandas as pd
import numpy as np

arr=np.arange(1,6)
s=pd.Series(arr)

print(arr)
print(s)
print(type(s))


#changing index...
s1=pd.Series(arr,index=['a','b','c','d','e'],dtype=float,name='python')
print(s1)
print(s1['a'])


#creating series by dict..

calories = {'day1':290,"day2": 380, "day3": 390}
s_calories=pd.Series(calories)
print(s_calories)
print(s_calories['day1'])



