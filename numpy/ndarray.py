import numpy as np
num_list=[1,2,3,4,5]
print(num_list)
ndarray=np.asarray(num_list)#asaarrayでリストをndarrayに変換
print(ndarray)
print(type(ndarray))#typeで型を確認
for i in ndarray:
    print(i)