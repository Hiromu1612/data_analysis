import numpy as np

x=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])
y=np.array([[9,8,7],
            [6,5,4],
            [3,2,1]])
print(x+y) #要素ごとの和


x=np.array([1,2,3]) #1行3列 1次元配列と多次元配列は最後の次元のサイズが一致していれば計算可能
y=np.array([4,5,6], #2行3列
            [7,8,9])
print(x+y) #要素ごとの和


x=np.array([[2], #3行1列 N行1列と多次元配列は最後から2番目の次元のサイズが一致していれば計算可能
            [4],
            [6]])
y=np.array([[5,6,7], #3行3列
            [8,9,10],
            [11,12,13]])
print(x+y) #要素ごとの和


x=np.array([[1,2,3], #2行3列
            [4,5,6]])
y=np.array([[7,8,9], #3行3列
            [10,11,12],
            [13,14,15]]) 
print(np.dot(x,y)) #数学の行列の積