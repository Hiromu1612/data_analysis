import pandas as pd
data={
    "A":["100","300"],
    "B":["200","1,500"]
}
df=pd.DataFrame(data)
df["A"]=df["A"].astype(int) #object(文字列型)をint(整数型)に変換
print(df.dtypes)

df["B"]=df["B"].str.replace(",","").astype(int) #カンマを削除してint型に変換
print(df.dtypes)