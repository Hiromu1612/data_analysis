from scipy.stats import norm

score_list=[60,70,80]
for score in score_list:
    cdf=norm.cdf(x=score,loc=50,scale=10)#累積分布関数CDF Cumulative Distribution Function ある範囲の確率を求める
    print("偏差値",score,"は上から",(1-cdf)*100,"%の位置にあります")

# %→値
percent_list=[0.1586,0.02275,0.00134]
for percent in percent_list:
    ppf=norm.ppf(q=(1-percent),loc=50,scale=10)#パーセント点関数 Percent Point Function ある確率を持つ値を求める
    print("上から",percent*100,"%の位置にある偏差値は",ppf,"です")