import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data={
    "クッキー":[35,47,18],
    "ケーキ":[20,30,50]
}
index=["好き","普通","嫌い"]
df=pd.DataFrame(data,index=index)

df["クッキー"].plot.pie(startangle=90,counterclock=False,labeldistance=0.5)#matplotlibの円グラフは右側から始まり、反時計回り 真上から始まり、時計回りに変更 凡例を内側に表示
plt.show()