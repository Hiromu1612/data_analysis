import numpy as np

list=[[1,2,3],
        [4,5,6]] #2行3列のリスト
x=np.array(list)
print(x.reshape(3,2)) #3行2列に変換
print(x.flatten()) #1次元配列に変換