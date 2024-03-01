from scipy.stats import norm

score_A=60
mean_A=50
std_A=5

score_B=80
mean_B=70
std_B=8

#値→%
cdf=norm.cdf(x=score_A,loc=mean_A,scale=std_A)#累積分布関数CDF Cumulative Distribution Function ある範囲の確率を求める
print("Aの点数",score_A,"は上から",(1-cdf)*100,"%の位置にあります")
cdf=norm.cdf(x=score_B,loc=mean_B,scale=std_B)#累積分布関数CDF Cumulative Distribution Function ある範囲の確率を求める
print("Bの点数",score_B,"は上から",(1-cdf)*100,"%の位置にあります")