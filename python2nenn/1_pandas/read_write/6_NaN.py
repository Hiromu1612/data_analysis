import pandas as pd
data={
    "国語":[90,50,None,70], #Noneは欠損値
    "数学":[60,None,None,85]
    }

index=["一郎","次郎","三郎","四郎"]
df=pd.DataFrame(data,index=index)
print(df)

print(df.isnull()) #欠損値をTrueで表示 nanの略はNot a Number
print(df.isnull().sum()) #欠損値の数を表示 int64は整数型のデータ
print(df.dropna()) #欠損値を含む行を削除 1つでも欠損値がある行を削除
print(df.dropna(subset=["国語"])) #国語列に欠損値がある行を削除
print(df.fillna(df.mean())) #欠損値を平均値で埋める
print(df.fillna(method="ffill")) #欠損値を1つ前の値で埋める 温度のように連続的に変化する場合はデータが上下しないようにできる ffillはforward fillの略
