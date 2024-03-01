import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data = {
    "ID": [0,1,2,3,4,5,6,7,8,9],
    "A" : [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
    "B" : [49, 50, 49, 54, 45, 52, 56, 48, 45, 52]
}
df = pd.DataFrame(data)

bins=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100] #binsに区切りたい値をリストで指定 binsは階級

df["A"].plot.hist(bins=bins,color="blue",figsize=(8,8),ylim=(0,6))
plt.title("Aのヒストグラム",fontsize=20)

A_mean=df["A"].mean()
A_std=df["A"].std()
plt.axvline(x=df["A"].mean(),color="red",linestyle="--") #平均値
plt.axvline(x=A_mean-A_std,color="blue",linestyle="--") #68%のデータを含む範囲
plt.axvline(x=A_mean+A_std,color="blue",linestyle="--") #68%のデータを含む範囲
plt.show()


df["B"].plot.hist(bins=bins,color="green",figsize=(8,8),ylim=(0,6))
plt.title("Bのヒストグラム",fontsize=20)

B_mean=df["B"].mean()
B_std=df["B"].std()
plt.axvline(x=df["B"].mean(),color="red",linestyle="--") #平均値
plt.axvline(x=B_mean-B_std,color="blue",linestyle="--") #68%のデータを含む範囲
plt.axvline(x=B_mean+B_std,color="blue",linestyle="--") #68%のデータを含む範囲
plt.show()