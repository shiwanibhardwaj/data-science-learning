import pandas as pd
dict={
    'names':['shivani','abhishek','saurabh'],
    'age':[22,24,26],
    'marks':[234,341,542]
}

data=pd.DataFrame(dict)
data.to_csv('data_file.csv' ,index=False ,header=[1,2,3])
print(data)