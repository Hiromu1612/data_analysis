import numpy as np

x=np.array([[1,2,3],
            [4,5,6]]) #2行3列
print(x.reshape(3,2))#reshapeで配列の形を変更

print(x.flatten()) #flattenで配列を1次元に変換