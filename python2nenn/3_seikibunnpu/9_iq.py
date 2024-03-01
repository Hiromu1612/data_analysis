from scipy.stats import norm

IQ_list=[110,130,148]
for IQ in IQ_list:
    cdf=norm.cdf(x=IQ,loc=100,scale=15)#累積分布関数CDF Cumulative Distribution Function ある範囲の確率を求める IQの標準偏差は15or24
    print("IQ",IQ,"は上から",(1-cdf)*100,"%の位置にあります")