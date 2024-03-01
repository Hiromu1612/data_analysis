import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data={
    "身長" :[163.6, 172.6, 163.7, 169.9, 173.9, 166.2, 176.7, 165.4],
    "体重" :[50.5, 63.3, 48.5, 59.8, 69.8, 53.7, 70.3, 51.2]
}
df=pd.DataFrame(data)
df.plot.scatter(x="身長",y="体重",color="blue",figsize=(12,8)) #scatterは散布図 figsizeで大きさを指定(横,縦) 単位はインチ

x=df.iloc[3]["身長"]
y=df.iloc[3]["体重"]
plt.plot(x,y,color="red",marker="X",markersize=15) #赤い点をプロット マーカーは×で大きさは15ポイント

plt.axvline(x=x,color="green",linestyle="--") #x軸 緑の破線を引く
plt.axhline(y=y,color="purple",linestyle=":") #y軸 紫の点線を引く

plt.show()