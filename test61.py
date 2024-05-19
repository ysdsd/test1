import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

iris = pd.read_excel("D:\QQ文件\实验6 复杂数据可视化\实验6 复杂数据可视化\经营数据.xls")
sns.pairplot(iris, hue='type', plot_kws={'alpha': 0.6, 's': 80, 'edgecolor': 'k'}, height=3)
plt.show()