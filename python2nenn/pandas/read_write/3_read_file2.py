import pandas as pd

df=pd.read_csv("python2nenn/sample/test.csv")

#列データを取り出す
print(df[["国語","数学"]])

#行データを取り出す
print(df.iloc[0:2])#0-2行目 ilocはindex location
print(df.loc[[0,2]])#0,2行目

#要素を一つ取り出す
print(df.iloc[0,1])#0行1列
print(df.loc[0,"国語"])#0行国語列