# 1）导入数据集

#导入pandas和有序字典
from collections import OrderedDict
import pandas as pd
# 绘制训练数据和测试数据的散点图
import matplotlib.pyplot as plt

# 使用机器学习包 建立训练和测试数据
# train_test_split是交叉验证中常用的函数，功能是从样本中随机的按比例选取训练数据（train）和测试数据（test）
from sklearn.model_selection import train_test_split

# 导入逻辑回归包
from sklearn.linear_model import LogisticRegression

#建立数据集 有序字典对数据集进行排序
examDict={
    '学习时间':[0.50,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,
            2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
    '通过考试':[0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1]
}
examOrderDict=OrderedDict(examDict)
examDf=pd.DataFrame(examOrderDict)
examDf.head(10)

# 2）提取特征和标签

#提取数据集对特征和标签
#特征features
exam_X=examDf.loc[:,'学习时间']
#标签labes
exam_y=examDf.loc[:,'通过考试']




def methord1():
    # 散点图  通过散点图看看两个变量的分布情况
    plt.scatter(exam_X, exam_y, color="b", label="exam data")

    # 添加图标标签
    plt.xlabel("Hours")
    plt.ylabel("Pass")
    # 显示图像
    plt.show()

def methord2():
    # 3）建立训练数据和测试数据

    # 建立训练数据和测试数据
    X_train, X_test, y_train, y_test = train_test_split(exam_X,
                                                        exam_y,
                                                        train_size=.8)
    # 输出数据大小
    print('原始数据特征：', exam_X.shape,
          '，训练数据特征：', X_train.shape,
          '，测试数据特征：', X_test.shape)

    print('原始数据标签：', exam_y.shape,
          '训练数据标签：', y_train.shape,
          '测试数据标签：', y_test.shape)

def methord3():
    # 4）绘制训练和测试数据散点图

    # 散点图
    plt.scatter(X_train, y_train, color="blue", label="train data")
    plt.scatter(X_test, y_test, color="red", label="test data")

    # 添加图标标签
    plt.legend(loc=2)
    plt.xlabel("Hours")
    plt.ylabel("Pass")
    # 显示图像
    plt.show()

def methord4():
    # 5）训练模型

    # 使用训练数据 训练模型 需要先将数据转化为数组 多行一列的数组
    # 将训练数据特征转换成二维数组X行*1列
    X_train = X_train.values.reshape(-1, 1)
    # 将测试数据特征转换成二维数组X行*1列
    X_test = X_test.values.reshape(-1, 1)

    # 创建模型：逻辑回归
    model = LogisticRegression()
    # 训练模型
    model.fit(X_train, y_train)

def methord5():
    # 6）评估模型（使用训练数据评估模型准确率）

    # 评估模型：准确率 score方法计算出的是正确率 测试数据的特征和标签
    model.score(X_test, y_test)


def methord6():
    # 7）决策面

    # 获取概率值第1个值是标签为0的概率值，第2个值是标签为1的概率值,两个值的和=1
    # 决策面 概率大于0.5等于标签为1的分类
    # model.predict_proba(4)
    model.predict_proba([[4]])

def methord7():
    # 8）预测数据

    # 预测数据：使用模型的predict方法可以进行预测。这里我们输入学生的特征学习时间4小时，模型返回结果标签是0，
    # 表示预测该学生通过考试。#决策面 概率大于0.5等于标签为1的分类
    pred = model.predict([[4]])
    print(pred)
def methord8():
    # 9）计算预测概率值 回归方程

    # 第1步：得到回归方程的z值
    # 回归方程：z= + x
    # 截距
    a = model.intercept_
    # 回归系数
    b = model.coef_

    x = 4
    z = a + b * x

    # 第2步：将z值带入逻辑回归函数中，得到概率值
    y_pred = 1 / (1 + np.exp(-z))
    print('预测的概率值：', y_pred)


if __name__ == "__main__":
    methord1()
    # print(f"分析完成，用时时间为{time.time() - start_time}秒")