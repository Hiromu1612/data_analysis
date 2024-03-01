import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="dark")#日本語フォントを指定

data = {
    "ID": [0,1,2,3,4,5,6,7,8,9],
    "A" : [59, 24, 62, 48, 58, 19, 32, 88, 47, 63],
    "B" : [49, 50, 49, 54, 45, 52, 56, 48, 45, 52]
}
df = pd.DataFrame(data)


mean_A=df["A"].mean()
std_A=df["A"].std()
print(mean_A-std_A,"~",mean_A+std_A) #平均±標準偏差は68%のデータを含む範囲

mean_B=df["B"].mean()
std_B=df["B"].std()
print(mean_B-std_B,"~",mean_B+std_B) #平均±標準偏差は68%のデータを含む範囲

df.plot.scatter(x="ID",y="A",color="blue",ylim=(0,100),figsize=(8,8))
plt.axhline(y=mean_A-std_A,color="red",linestyle="--") #axvlineはx軸に線を引く axhlineはy軸に線を引く
plt.axhline(y=mean_A+std_A,color="blue",linestyle="--")
plt.title("Aの散布図",fontsize=20)
plt.show()

df.plot.scatter(x="ID",y="B",color="green",ylim=(0,100),figsize=(8,8))
plt.axhline(y=mean_B-std_B,color="red",linestyle="--")
plt.axhline(y=mean_B+std_B,color="blue",linestyle="--")
plt.title("Bの散布図",fontsize=20)
plt.show()