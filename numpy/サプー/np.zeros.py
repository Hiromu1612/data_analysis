import numpy as np

x=np.zeros(3) #1次元配列で3つの要素を0で初期化
print(x)
x=np.zeros((2,3)) #2行3列の配列を0で初期化
print(x)

x=np.ones(3) #1次元配列で3つの要素を1で初期化
print(x)

z=np.random.rand(3) #0-1の範囲の乱数で3つの要素を初期化
print(z)

z=np.empty(3) #3つの要素を初期化 0に近い値が入る 0で初期化するときよりもメモリからそのまま取り出すため高速
print(z)