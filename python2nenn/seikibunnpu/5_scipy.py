#scipyはscience+pythonの略で、科学技術計算を行うためのライブラリ
#scipyはnumpyをベースにしているため、numpyの関数を利用することができる
from scipy.stats import norm #statsは統計学, normは正規分布のライブラリ
import time
start=time.perf_counter()
mean=166.8
sd=5.8 #標準偏差 standard deviation 分散はvariance
value=160.0

#値→%
cdf=norm.cdf(x=value,loc=mean,scale=sd)#累積分布関数CDF Cumulative Distribution Function ある範囲の確率を求める 調べたい値,平均,標準偏差
print(value,"は下から",cdf*100,"%の位置にあります")
print(value,"は上から",(1-cdf)*100,"%の位置にあります")

# %→値
ppf=norm.ppf(q=0.95,loc=mean,scale=sd)#パーセント点関数 Percent Point Function ある確率を持つ値を求める
print("下から95%の値は",ppf,"です")
print("上から5%の値は",norm.ppf(q=0.05,loc=mean,scale=sd),"です")
end=time.perf_counter()
print("処理時間",(end-start)*1000,"s")