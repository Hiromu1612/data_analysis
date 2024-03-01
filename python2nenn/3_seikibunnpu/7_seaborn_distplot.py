import pandas as pd, matplotlib.pyplot as plt,seaborn as sns, seaborn as sns, numpy as np
from scipy.stats import norm
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="dark")#日本語フォントを指定

data={
    "A":np.random.randint(0,100,1500), #最小値0,最大値100,15個の乱数 偏りのない一様分布のような値
    "B":np.random.normal(50,10,1500), #平均50,標準偏差10,15個の乱数 中央値が多い正規分布のような値
}

df=pd.DataFrame(data)

sns.distplot(df["A"],fit=norm,fit_kws={"color":"red"})# displotはseabornでもっとデータがあった場合の予測カーブ(カーネル密度推定) fit=normで正規分布のカーブを表示 fit_kwsで色を指定
plt.title("Aの分布", fontsize=20)
plt.show()

sns.distplot(df["B"],fit=norm,fit_kws={"color":"red"})
plt.title("Bの分布", fontsize=20)
plt.show()