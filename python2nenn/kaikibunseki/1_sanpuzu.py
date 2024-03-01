import matplotlib.pyplot as plt,pandas as pd,seaborn as sns
# sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="whitegrid")#日本語フォントを指定
import japanize_matplotlib #日本語フォントを指定

data = {
    "数学" : [100, 85, 90, 95, 80, 80, 75, 65, 65, 60, 55, 45, 45],
    "理科" : [94, 90, 95, 90, 85, 80, 75, 70, 60, 60, 50, 50, 48],
    "社会" : [80, 88, 70, 62, 86, 70, 79, 65, 75, 67, 75, 68, 60]
}
df=pd.DataFrame(data)

#相関係数を求める
print("数学と理科の相関係数",df.corr()["数学"]["理科"]) #0.96で強い正の相関 横,縦の列
print("数学と社会の相関係数",df.corr()["数学"]["社会"]) #0.39で弱い正の相関
print(df.corr()) #列名の指定がいないと相関係数行列を表示 corrはcorrelation(相関)の略

df.plot.scatter(x="数学",y="理科",color="blue",label="数学と理科")
sns.regplot(data=df,x="数学",y="理科",line_kws={"color":"red"}) #回帰直線を表示 誤差が一番少なくなる直線 regplotはregression(回帰) plot kwsはkeyword arguments
plt.title("数学と理科の相関", fontsize=20) #薄い赤い範囲は信頼区間(95%の確率でこの範囲に含まれる) 信頼区間が広いと信頼性が低い
sns.jointplot(data=df,x="数学",y="理科",kind="reg",line_kws={"color":"red"}) #kind="reg"で回帰直線を表示 ヒストグラムを追加
plt.show()

df.plot.scatter(x="数学",y="社会",color="red",label="数学と社会")
sns.regplot(data=df,x="数学",y="社会",line_kws={"color":"blue"})
plt.title("数学と社会の相関", fontsize=20)
sns.jointplot(data=df,x="数学",y="社会",kind="reg",line_kws={"color":"blue"})
plt.show()