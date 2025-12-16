import pandas as pd

#read csv files
df=pd.read_csv('data.csv',nrows=1,usecols=["columns name"],skiprows=['row indexes'],index_col='column name')   #if u want only one raw.
print(df.index) 
print(df.sort_index(axis=0,ascending=False))
df.loc["row", 'column name']='anything that u want to change.' #if u want to make change.
df.icol['row', 'column index']
df.drop('column names',axis=1) #for row pass row index and axis=0
#read excel files
df=pd.read_excel("data.excel")

#read JSON files
df=pd.read_json("data.excel")

print(df.to_string())
#to_string will print the entire dataframe.


pd.options.display.max_rows = 9999 #Increase the maximum number of rows to display the entire DataFrame.
df = pd.read_csv('data.csv')
print(df) 

