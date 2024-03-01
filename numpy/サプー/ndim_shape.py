import numpy as np

x1=np.array([1,2,3])
x2=np.array([[1,2,3],
                [4,5,6]])
x3=np.array([[[1,2,3],
                [4,5,6],
                    [7,8,9]]])
print(x1.ndim) #1次元配列
print(x2.ndim) #2次元配列
print(x3.ndim) #3次元配列

print(x1.shape) #1次元配列で3つの要素 3
print(x2.shape) #2行3列の配列 2,3
print(x3.shape) #2行3列の配列 []の外側から順に行、列、深さ 1,3,3