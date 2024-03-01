import pandas as pd
data=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]

df=pd.DataFrame(data)
df.columns=['国語','数学','英語']
df.index=['一郎','次郎','三郎']

print(df)

#最初からヘッダーとインデックスを指定してデータフレームを作成
data=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
columns=['国語','数学','英語']
index=['一郎','次郎','三郎']

df=pd.DataFrame(data,columns=columns,index=index)
print(df)

#辞書型からデータフレームを作成
data={
    '国語':[10,40,70],#キーが列のヘッダーになる
    '数学':[20,50,80],
    '英語':[30,60,90]
}
index=['一郎','次郎','三郎']
df=pd.DataFrame(data,index=index)
print(df)