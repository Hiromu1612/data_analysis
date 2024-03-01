import numpy as np
num_list=[[1,2,3],
            [4,5,6],
                [7,8,9]]
ndarray=np.asarray(num_list) #asaarrayでリストをndarrayに変換
print(ndarray)
#ndarray→リスト
ndarray_list=ndarray.tolist()
print(ndarray_list)