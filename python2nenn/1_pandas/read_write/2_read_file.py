import pandas as pd

df=pd.read_csv("python2nenn/sample/test.csv")#encoding="shift-jis"を追加すると文字化けを防げる
# print(df)

df=pd.read_csv("python2nenn/sample/test.csv")#index_col=0で1列目をインデックスに指定
# print(df)

# print(df.head())#先頭5行を表示
# print(df.tail())#末尾5行を表示
# print(df.head(3))#先頭3行を表示
# print(df.index)#インデックスを表示

list1=df.columns.tolist()#インデックスをリストに変換
print(list1)

print(df.dtypes)#データ型を表示 整数はint64、小数はfloat64、文字列はobject

print(len(df.index))#行数を表示
print(len(df.columns))#列数を表示