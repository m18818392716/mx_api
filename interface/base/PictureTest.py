import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
from .mplot3d import Axes3D

#1、线型图
# df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('2018/12/18',periods=10), columns=list('ABCD'))
# df.plot()
# plt.show()

# s = Series( np. random. randn( 10). cumsum(), index= np. arange( 0, 100, 10))
# s.plot()
# plt.show()

#2、


#3、条形图
# 水平条形图
# df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df.plot.bar(stacked=True)
# plt.show()

# 堆积条形图
# df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# df.plot.barh(stacked=True)
# plt.show()

# #4、直方图
# df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000), 'c':
# np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
# df.plot.hist(bins=20)
# plt.show()
#
# #5、箱型图
# df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
# df.plot.box()
# plt.show()
#
#
#
# 6、块型图
# df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
# df.plot.area()
# plt.show()
#
#
# 7、散点图
# df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
# # df.plot.scatter(x='a', y='b')
# # plt.show()
#
# 8、饼状图
# df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
# df.plot.pie(subplots=True)
# plt.show()

# 8、饼状图-一般饼图
# labels = 'A', 'B', 'C', 'D'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0.1, 0)
# plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
# shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

# 8、饼状图-嵌套饼图
# size = 0.3
# vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
# cmap = plt.get_cmap("tab20c")
# outer_colors = cmap(np.arange(3)*4)
# inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))
# print(vals.sum(axis=1))
# # [92. 77. 39.]
# plt.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
# wedgeprops=dict(width=size, edgecolor='w'))
# print(vals.flatten())
# # [60. 32. 37. 40. 29. 10.]
# plt.pie(vals.flatten(), radius=1-size, colors=inner_colors,
# wedgeprops=dict(width=size, edgecolor='w'))
# # equal makes it a perfect circle
# plt.axis('equal')
# plt.show()

# 8、饼状图-极轴饼图
# np.random.seed(19680801)
# N = 10
# theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
# radii = 10 * np.random.rand(N)
# width = np.pi / 4 * np.random.rand(N)
# ax = plt.subplot(111, projection='polar')
# bars = ax.bar(theta, radii, width=width, bottom=0.0)
# for r, bar in zip(radii, bars):bar.set_facecolor(plt.cm.viridis(r / 10.))
# bar.set_alpha(0.5)
# plt.show()

# 散点图-三维散点图
# data = np.random.randint(0, 255, size=[40, 40, 40])
# x, y, z = data[0], data[1], data[2]
# ax = plt.subplot(111, projection='3d')
# ax.scatter(x[:10], y[:10], z[:10], c='y')
# ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
# ax.scatter(x[30:40], y[30:40], z[30:40], c='g')
# ax.set_zlabel('Z')
# ax.set_ylabel('Y')
# ax.set_xlabel('X')
# plt.show()

# 三维平面图
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
plt.savefig('fig.png',bbox_inches='tight')
# plt.show()

# 平行条形图
# 此例中，我们引入三组（a,b,c）5个随机数（0~1），并用条形图打印出来，做比较
size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)
total_width, n = 0.8, 3
width = total_width / n
# redraw the coordinates of x
x = x - (total_width - width) / 2
# here is the offset
plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
plt.show()
