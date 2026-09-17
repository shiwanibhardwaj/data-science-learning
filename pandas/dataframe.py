import pandas as pd

data = {
    "Name": ["Amit", "Riya", "John", "Sara", "Vikram"],
    "Age": [23, 12, 15, 22, 24],
    "City": ["Delhi", "Mumbai", "New York", "London", "Bangalore"],
    "Score": [85, 92, 78, 90, 88]
}

df=pd.DataFrame(data)
print(df)
print(df[2:4]) 



print(df.head(2))   #First 2 rows
print(df.tail(2))   #last 2 rows
print(df.shape)     #Shape (rows, columns)
print(df.columns)   #columns name
print(df.dtypes)    #data types
print(df.describe()) #Summary statistics (numeric columns)
print(df.info())     #Full information (very important).
print(df.index)
print(df.sample(5))   #it will print some random samples of a dataset.  
print(df.nunique())
print(df.to_string())    #it will print all the dataset.
#arithmetic operations....
df['values']=df['Age']+df['Score']
print(df)

df['values']=df['Age']-df['Score'] #we can perform other arithmetic operations.
print(df)

#finding data...
df['info']=df['Age'] < 20
print(df)

print(df["Age"]<=20)


#by list inside list
info=[['saurabh',28],["shivani",22],['abhishek',26]]
df=pd.DataFrame(info,columns=["names","ages"])
print(df)


#dataframe by numpy array..
import numpy as np
data=np.array([[1,2,3],[4,5,6],[7,8,9]])
df=pd.DataFrame(data,columns=["A","B","C"])
print(df)


data = pd.read_csv("D:/shivani/data science/pandas/titanic/train.csv")
#selecting data row wise (loc,iloc)
print(data.loc[2])
print(data.loc[5:11])  #start index:end index (inclusive)

print(data.iloc[2])
print(data.iloc[5:11])  #start index:end index (exclusive)

#cells-row,col
print(data.loc[2,["Name",'Age']])
print(data.iloc[2:9,2:5])

print(data.at[2,'Name'])
print(data.iat[2,3])