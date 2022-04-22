import pandas as pd

df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))

def max_common(df_a, df_b):
    df_out = pd.concat([df_a, df_b]).max(level=0)
    df_out = pd.DataFrame(data=df_out, columns=df_a.columns)
    return df_out

def max_common2(df_a, df_b):
    df_out = pd.DataFrame(data=[])
    
    for col_a in df_a.columns:
        if col_a not in df_b.columns:
            df_out[col_a] = df_a[col_a]
        else:
            df_out[col_a] = df_a[col_a].where(df_a[col_a] > df_b[col_a], other=df_b[col_a])
    return df_out

print(max_common2(df_a, df_b))