from collections import OrderedDict
import pandas as pd

# 理解数据 原始数据集 有序字典排序
examDict={
    '学习时间':[0.50,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,
            2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
    '分数':    [10,  22,  13,  43,  20,  22,  33,  50,  62,
              48,  55,  75,  62,  73,  81,  76,  64,  82,  90,  93]
}
examOrderDict=OrderedDict(examDict)
examDf=pd.DataFrame(examOrderDict)



# 画出数据集散点图
#提取数据的特征和标签 学习时间是特征 标签是分数
#特征features
exam_X=examDf.loc[:,'学习时间']
#标签labes
exam_y=examDf.loc[:,'分数']


#绘制散点图 使用绘图包matplotlib
import matplotlib.pyplot as plt

#散点图
plt.scatter(exam_X, exam_y, color="b", label="exam data")

#添加图标标签
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()


# 计算相关系数
#相关系数：corr返回结果是一个数据框，存放的是相关系数矩阵
rDf=examDf.corr()
print('相关系数矩阵：')
rDf



# 建立训练数据和测试数据
#特征features _X表示标签
exam_X=examDf.loc[:,'学习时间']
#标签labes _y表示标签
exam_y=examDf.loc[:,'分数']

from sklearn.model_selection import train_test_split


#建立训练数据和测试数据  表示训练和测试数据的标签和特征
X_train , X_test , y_train , y_test = train_test_split(exam_X ,
                                                       exam_y ,
                                                       train_size = 0.8)
#输出数据大小
print('原始数据特征：',exam_X.shape ,
      '，训练数据特征：', X_train.shape ,
      '，测试数据特征：',X_test.shape )

print('原始数据标签：',exam_y.shape ,
      '训练数据标签：', y_train.shape ,
      '测试数据标签：' ,y_test.shape)



# 训练模型（使用训练数据）
X_train=X_train.values.reshape(-1,1)
X_test=X_test.values.reshape(-1,1)
#第1步：导入线性回归
from sklearn.linear_model import LinearRegression
# 第2步：创建模型：线性回归
model = LinearRegression()
#第3步：训练模型
model.fit(X_train , y_train)



# 计算最佳拟合线方程
#截距
a=model.intercept_
#回归系数
b=model.coef_

print('最佳拟合线：截距a=',a,'，回归系数b=',b)


# 画出最佳拟合线 训练数据
#绘散点图 并画出最佳拟合线
import matplotlib.pyplot as plt
#训练数据散点图
plt.scatter(X_train, y_train, color='blue', label="train data")

# 训练数据的预测值
y_train_pred = model.predict(X_train)
#绘制最佳拟合线
plt.plot(X_train, y_train_pred, color='black', linewidth=3, label="best line")

#添加图标标签
plt.legend(loc=2)
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()


# 模型评估（使用测试数据）
#线性回归的scroe方法得到的是决定系数R平方
#评估模型:决定系数R平方
model.score(X_test , y_test)


# 画出最后的最佳拟合线（训练数据和测试数据）
#导入绘图包
import matplotlib.pyplot as plt
plt.scatter(X_train, y_train, color='blue', label="train data")
#最佳拟合线训练数据的预测值
y_train_pred = model.predict(X_train)
#绘制最佳拟合线：标签用的是训练数据的预测值y_train_pred
plt.plot(X_train, y_train_pred, color='black', linewidth=3, label="best line")

plt.scatter(X_test, y_test, color='red', label="test data")

#添加图标标签
plt.legend(loc=2)
plt.xlabel("Hours")
plt.ylabel("Score")
#显示图像
plt.show()


#

