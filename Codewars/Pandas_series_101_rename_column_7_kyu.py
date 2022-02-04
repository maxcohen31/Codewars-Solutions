import pandas as pd
def rename_columns(df, names):
    return pd.DataFrame(data=df.values, columns=names)
     

# Solution 2
def rename_columns2(df, names):
    df.rename(columns=dict(zip(df.columns, names)), inplace=True)
    return df
 
df1 = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
names = ('A', 'B', 'C')


