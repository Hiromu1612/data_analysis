import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定
data={
    "名前":["A","B","C","D","E"],
    "国語":[80,95,70,60,100],
    "数学":[70,46,80,90,100],
    "英語":[100,100,100,100,100]
}
df=pd.DataFrame(data)
df.set_index("名前",inplace=True) #名前をインデックスにする インデックス番号は見づらいため

df.plot.bar()
plt.title("成績")
plt.show()

df["国語"].plot.bar()
plt.title("国語の成績")
plt.show()