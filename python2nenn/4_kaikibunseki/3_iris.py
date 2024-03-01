import pandas as pd
import seaborn as sns
import japanize_matplotlib

import matplotlib.pyplot as plt

df = sns.load_dataset("iris")
print(df.head())

mapping = {'setosa': 1.0, 'versicolor': 2.0, 'virginica': 3.0} #setosaはセトサ, versicolorはバージカラー, virginicaはバージニカ
df['species'] = df['species'].map(mapping)
print(df.corr())

plt.figure(figsize=(8, 8))  # サイズを指定
sns.heatmap(df.corr(), annot=True, vmax=1, vmin=-1, center=0)
plt.show()

sns.pairplot(data=df, hue="species", kind="reg")  # kind="reg"で回帰直線を表示, hue="species"で種類ごとに色分け hueは色合い
plt.show()