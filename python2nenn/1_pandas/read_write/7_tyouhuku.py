import pandas as pd
data=[
    [10,30,40],
    [20,30,40],
    [10,30,40],
    [20,30,40]
]
df=pd.DataFrame(data)
print(df.duplicated().value_counts())#重複行をカウント 打ち間違いで重複する場合がある
print(df.drop_duplicates())#重複行を削除