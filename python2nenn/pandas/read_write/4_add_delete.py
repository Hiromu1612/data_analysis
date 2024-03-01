import pandas as pd #フォルダ名を日本語にするとエラーになるので注意

df_A=pd.read_csv("python2nenn/sample/test.csv",index_col=0)
df_B=pd.DataFrame() #空のデータフレームを作成

#列を追加
df_B["国語"]=df_A["国語"]
print(df_B)

#行を追加
# df_B=df_B.append(df_A.iloc[0]) pandas2.1.1では廃止されている
# print(df_B)

#列を削除
df_A=df_A.drop("国語",axis=1) #axis=1で列を指定 axis=0で行を指定
print(df_A)

#行を削除
df_A=df_A.drop("B介",axis=0) #df_A=df_A.drop(df_A.index[0])でも可
print(df_A)