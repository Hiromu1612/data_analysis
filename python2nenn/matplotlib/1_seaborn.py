import matplotlib.pyplot as plt

# plt.plot([0,100,200],
#         [100,0,200])
# plt.show()

import seaborn as sns
sns.set(font=["Meiryo","Yu Gothic","Hiragino Maru Gothic Pro"],style="dark")#日本語フォントを指定

plt.plot([0,100,200],
        [100,200,200])
plt.title("タイトル")
plt.xlabel("横軸")
plt.ylabel("縦軸")
plt.show()