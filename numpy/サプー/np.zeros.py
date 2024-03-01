import numpy as np

x=np.zeros(3) #1次元配列で3要素
print(x)
x=np.zeros((2,3)) #2次元配列で2行3列
print(x)

y=np.ones(3) #1次元配列で3要素
print(y)

z=np.random.rand(3) #1次元配列で3要素 0-1の乱数
print(z)

z=np.empty(3) #1次元配列で3要素 0で初期化された配列 要素を返還せずにメモリからそのまま取り出すため高速
print(z)