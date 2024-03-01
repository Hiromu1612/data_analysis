import numpy as np

x_1=np.array([1,2,3])

x_2=np.array([[1,2,3],
                [4,5,6]])

x_3=np.array([[[1,2,3],
                [4,5,6],
                    [7,8,9]]])

print(x_1.ndim)#次元数
print(x_2.ndim)
print(x_3.ndim)

print(x_1.shape)#形状 1次元配列で3要素
print(x_2.shape) #2次元配列で2行3列
print(x_3.shape) #3次元配列で1行3列3深さ []の外側から順に行、列、深さ