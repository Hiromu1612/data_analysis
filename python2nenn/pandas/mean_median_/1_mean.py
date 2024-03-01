import pandas as pd
data={
    "A":[80,95,70],
    "B":[70,46,80],
}
df=pd.DataFrame(data)

print(df["A"].mean()) #平均値を求める
print(df.iloc[1]["A"])