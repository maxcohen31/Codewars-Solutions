import pandas as pd

def flatten(dataframe, col): 
    new_df = dataframe.explode(col)
    return new_df.set_index(pd.Index(range(len(new_df[col]))))

df2 = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))

print(flatten(df2, 'A'))

