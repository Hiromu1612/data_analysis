import csv

header=["A","B","C"]
data=[[1,2,3],
      [4,5,6],
      [7,8,9]]

with open('test_w.csv', 'w',encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator='\n')# 改行コード（\n）を指定しておく
    writer.writerow(header)
    writer.writerows(data)