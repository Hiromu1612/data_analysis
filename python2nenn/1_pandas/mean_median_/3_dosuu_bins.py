import pandas as pd
data={
    "A":[1,10,1,10,1,10,1,10],
    "B":[5,5,5,5,6,6,6,6],
    "C":[1,2,3,4,7,8,9,10]
}
df=pd.DataFrame(data)
# print(df.mean())
# print(df.median())
# print(df.mode())
bins=[1,3,5,7,9,11] #binsに区切りたい値をリストで指定 binsは階級
cut=pd.cut(df["A"],bins=bins,right=False) #cut関数で区切りを指定 right=Falseで左側が閉区間になる 1≦x<3
table=cut.value_counts(sort=False) #value_countsで度数分布表を作成 sort=Falseでインデックスの順番を保持
print(table)

cut=pd.cut(df["B"],bins=bins,right=False)
table=cut.value_counts(sort=False)
print(table)

cut=pd.cut(df["C"],bins=bins,right=False)
table=cut.value_counts(sort=False)
print(table)