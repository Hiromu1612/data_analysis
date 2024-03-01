import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data={
    "Aクラス" :[163.6, 172.6, 163.7, 167.1, 169.9, 173.9, 170.1, 166.2, 176.7, 165.4],
    "Bクラス" :[166.9, 172.7, 166.4, 173.4, 169.6, 171.8, 166.9, 168.2, 166.7, 169.8]
}
df=pd.DataFrame(data)

df.plot.box()
plt.show()

sns.boxplot(data=df,width=0.2) #色付きで見やすい
plt.show()