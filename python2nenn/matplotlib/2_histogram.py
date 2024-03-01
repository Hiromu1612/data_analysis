import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定
data={
    "A":[1,10,1,10,1,10,1,10],
    "B":[5,5,5,5,6,6,6,6],
    "C":[1,2,3,4,7,8,9,10]
}
df=pd.DataFrame(data)
bins=[1,3,5,7,9,11]
df.plot.hist(bins=6,alpha=0.9,range=(0,11))#alphaで透明度を指定 6つの階級に分ける
# plt.xlim(1,10)
plt.title("ケーキの感想はどのように違うのか")
plt.xlabel("階級")
plt.show()

df["A"].plot.hist(bins=bins)
plt.title("ケーキAの感想はどのように違うのか")
plt.show()