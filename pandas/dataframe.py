import pandas as pd

data = {
    "Name": ["Amit", "Riya", "John", "Sara", "Vikram"],
    "Age": [23, 21, 25, 22, 24],
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
print(df.info())     #Full information (very important)