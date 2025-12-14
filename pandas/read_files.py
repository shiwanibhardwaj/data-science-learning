import pandas as pd

#read csv files
df=pd.read_csv('data.csv')  

#read excel files
df=pd.read_excel("data.excel")

#read JSON files
df=pd.read_json("data.excel")

print(df.to_string())
#to_string will print the entire dataframe.


pd.options.display.max_rows = 9999 #Increase the maximum number of rows to display the entire DataFrame.
df = pd.read_csv('data.csv')
print(df) 

