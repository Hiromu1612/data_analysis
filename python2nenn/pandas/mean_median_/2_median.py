import pandas as pd
data={
    "予想価格":[240,250,150,240,300,5000]
}
df=pd.DataFrame(data)
print(df.mean()) #平均値は外れ値に影響されやすい
print(df.median()) #中央値は外れ値に影響されにくい
print(df.mode()) #最頻値
