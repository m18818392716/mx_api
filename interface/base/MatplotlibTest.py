# 引入画图包并做全局设置
import seaborn as sns
#seaborn是在Matplotlib上封装的，为了使用其样式我们引入这个包。
import matplotlib
#引入matplotlib
import matplotlib.pyplot as plt
#我们需要用pylplot来画图
sns.set_style("whitegrid")
#我们选whitegrid主题样式
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.fontsize='20'
#这一段设置了中文支持的字体，字体大小

# 建立画布
fig, axs = plt.subplots(1, 2, figsize=(15,6), sharey=True)

# subplots(1, 2) 创建了包含一行两列的画布，即两个 axes 实例。
# figsize 确定了画布大小，sharey 控制共享坐标轴。如果没有子图，那么 fig=plt.figure() 就可以。

# 开始画饼图
labels = list(tpie.index)  # label是一个大蛋糕切开后，每一块的名字。
sizes = list(tpie['18年市场占比'])  # 这里确定了每块重多少。
explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0)  # 确定每块离中心位置多远

axs[0].pie(sizes, explode=explode, labels=labels, autopct='%1.2f%%', shadow=False, startangle=45,
           textprops={'fontsize': 18})
axs[0].set_title('18年1-3季度', fontsize='20')
axs[0].axis('equal')

# axs[0]：表示画布上第一块要画图了，pie 表示饼，plot 是线，bar 是柱。
# autopct：会把 sizes 换算成百分数。
# shadow：确定是否画阴影。
# textprops：配置数据标签字体大小。
# set_title：给第一个子图来个标题。
# axis('equal')：保证画出来的圆不会变扁。

# 保存图像
sizes = list(tpie['17年市场占比'])
explode = (0.0,0.0,0.0, 0.0,0.0,0.0)
axs[1].pie(sizes, explode=explode, labels=labels,autopct='%1.2f%%',shadow=False, startangle=45,textprops={'fontsize': 18})
axs[1].set_title('17年1-3季度',fontsize='20')
axs[1].axis('equal')
plt.savefig('e:/tj/month/fx1809/份额.png',dpi=600,bbox_inches = 'tight')
plt.show()


# axs[1]：开始了画第二个子图。
# plt.savefig：用来保存图像，第一个参数是存储文件位置及文件名，dpi 用来确定输出图像分辩率。
# plt.show()：在 Jupyter Notebook 中显示图像。