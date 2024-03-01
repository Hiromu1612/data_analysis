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

print(df.var()) #分散を求める 二乗したから平方根で元の単位に戻すと varの略はvariance
print(df.std()) #標準偏差を求める 大きいとばらつきが大きい stdの略はstandard deviation

df.plot.scatter(x="ID",y="A",color="blue",ylim=(0,100),figsize=(8,8))
plt.axhline(y=50,color="red",linestyle="--")
plt.title("Aの散布図",fontsize=20)
plt.show()

df.plot.scatter(x="ID",y="B",color="green",ylim=(0,100),figsize=(8,8))
plt.axhline(y=50,color="red",linestyle="--")
plt.title("Bの散布図",fontsize=20)
plt.show()