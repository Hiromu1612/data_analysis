import matplotlib.pyplot as plt,pandas as pd,seaborn as sns
import time
import matplotlib.style as mplstyle
mplstyle.use("fast") #高速モード
start = time.time()
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定

data = {
    "数学" : [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
    "理科" : [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
    "社会" : [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60]
}
df=pd.DataFrame(data)

#相関行列をヒートマップで表示
sns.heatmap(df.corr(),annot=True,vmax=1,vmin=-1,center=0) #annot=Trueで数値を表示 vmax,vminでカラーバーの最大値、最小値を指定 centerで中心値(相関なし)を0
plt.show()

#散布行列(散布図のすべての組を行列で表示) pairplotはpairwise(相互)の略 斜めの部分は同じデータ同士だから、散布図の代わりにヒストグラム
sns.pairplot(data=df,kind="reg") #kind="reg"で回帰直線を表示
plt.show()

print("time:",time.time()-start)