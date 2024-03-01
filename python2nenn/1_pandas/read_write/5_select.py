import pandas as pd

df_A=pd.read_csv("python2nenn/sample/test.csv",index_col=0)
df_A_80=df_A["国語"]>80
print(df_A_80) #条件に合致した行をTrue、合致しない行をFalseで表示

df_A_80=df_A[df_A["国語"]>80]
print(df_A_80) #条件に合致した行のみを表示

df_A_80_and=df_A[(df_A["国語"]>80) & (df_A["数学"]>80)] #()で条件を囲む
print(df_A_80_and) 