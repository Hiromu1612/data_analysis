import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data={
    "月" :  [1,2,3,4,5,6,7,8,9,10,11,12],
    "東京" : [5.6, 7.2, 10.6, 13.6, 20.0, 21.8, 24.1, 28.4, 25.1, 19.4, 13.1, 8.5],
    "那覇" : [18.1, 20.0, 19.9, 22.3, 24.2, 26.5, 28.9, 29.2, 28.0, 26.0, 23.1, 20.0],
    "札幌" : [-3.0, -2.6, 2.5, 8.0, 15.7, 17.4, 21.7, 22.5, 19.3, 13.3, 3.9, -0.8]
}

df=pd.DataFrame(data)
df.set_index("月",inplace=True) #月をインデックスにする
df.plot()
plt.title("気温の推移")
plt.xlabel("月")
plt.ylabel("気温")
plt.show()