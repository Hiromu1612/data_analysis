import random, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="dark")#日本語フォントを指定

#ガルトンボードのシミュレーション
def galton(steps,count):
    ans=[]#球が落ちた位置を記録するリスト
    for i in range(count):
        val=50 #球を最初に落とす初期位置 49,51に落ち、次は48,50,52
        for j in range(steps):
            if random.randint(0,1)==0: #0か1のどちらかをランダムに選ぶ
                val=val-1 #左に1つ移動
            else:
                val=val+1 #右に1つ移動
        ans.append(val)

    df=pd.DataFrame(ans)
    df[0].plot.hist()#0列目(落とした結果の列)
    plt.title("ガルトンボード " + str(steps) + "段:" + str(count) + "個", fontsize=20)
    plt.show()

galton(100,10000)