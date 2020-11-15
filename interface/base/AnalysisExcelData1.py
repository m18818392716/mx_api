import pandas as pd
import numpy as np

#读取数据
filename = 'F:\ChaoYang.xlsx'
# xls = pd.ExcelFile(filename,dtype='object')
xls = pd.ExcelFile(filename)
salesdf = xls.parse('Sheet1',dtype='object')
#打印出前5行数据
print(salesdf.head())

#数据大小，多少行多少列，注意shape后面不添加括号
print(salesdf.shape)

#数据类型:dtypes.后面也是不添加括号
print(salesdf.dtypes)

#数据清洗

#1）更改数据列头名字
"""
inplace=True是数据框本身会改动
inplace=False数据框本身不会变，而会创建一个改动后的新的数据框，默认的是flase

"""
dictnamecol={"购药时间":"销售时间"}
salesdf.rename(columns=dictnamecol,inplace=True)
print(salesdf.head())

#2) 缺失值处理
print("缺失前的数据大小：",salesdf.shape)
salesdf=salesdf.dropna(subset=["销售时间",'社保卡号'],how="any")
print("删除缺失后的大小：",salesdf.shape)

"""
数据类型的转换：字符串转为日期
销售数量和金额：字符串转为浮点型，有利于下面的describe进行统计，否则describe就会无法对销售数量和金额进行统计
"""
salesdf.loc[:,"销售数量"]=salesdf.loc[:,'销售数量'].astype("float")
salesdf.loc[:,"应收金额"]=salesdf.loc[:,'应收金额'].astype("float")
salesdf.loc[:,"实收金额"]=salesdf.loc[:,'实收金额'].astype("float")

#数据类型的转换
#定义一个函数，将列表中的字符串时间数据分列开，取第一个年月日，
def splitsaletime(timecolser):
    timelist=[]
    for value in timecolser:
        datastr=value.split(" ")[0]
        timelist.append(datastr)
    timeser=pd.Series(timelist)
    return timeser

#将excel中的第一行销售时间提取出来，运用到函数里面，再将提取出来的字符串年月日赋值给销售时间
timeser=salesdf.loc[:,'销售时间']
dataser=splitsaletime(timeser)
salesdf.loc[:,'销售时间']=dataser


"""
数据类型的转换：字符串转为日期
"""
#errors='coerce' 如果原始数据不符合日期的格式，转换后的值为空值NaT
#format 是原数据中的日期格式
salesdf.loc[:,'销售时间']=pd.to_datetime(salesdf.loc[:,"销售时间"],format='%Y-%m-%d',errors="coerce")
print(salesdf.dtypes)
#以上是销售时间从重命名，分列，获取年月日，再将年月日赋值给销售时间

#转换日期过程中不符合日期格式的数值会被转换为空值，
#这里删除列（销售时间，社保卡号）中为空的行
salesdf=salesdf.dropna(subset=['销售时间','社保卡号'],how='any')
print(salesdf.head())


#数据排序
"""
by:按哪一列排序
ascending=True，按照降序排列
ascending=False 按照升序排列
"""
#按照销售日期进行升序排列

salesdf=salesdf.sort_values(by="销售时间",ascending=True)
print(salesdf.head())

#经过重新排序后，index的索引列就会重新改变
#重命名行名（index）：排序后的列索引值是之前的行号，需要修改成从0到N的按顺序的索引值

salesdf=salesdf.reset_index(drop=True)
print(salesdf.head())

#异常值处理
print(salesdf.describe())
#发现存在的销售数量<0的异常值

#删除异常值：通过条件筛选出数据
#查询条件
queryser=salesdf.loc[:,"销售数量"]>0
#应用查询条件
print("删除异常值前：",salesdf.shape)
salesdf=salesdf.loc[queryser,:]#布尔运算,因为上面的查询条件得到的是行，所以根据布尔索引行对应相应的行。
print("删除异常值后：",salesdf.shape)



#构建模型
#指标1：月平均消费次数
"""
总消费次数：同一天，同一个人的所有消费都算作是一次消费
根据列名（销售时间，社区卡号），如果这两个列值同时相同，只保留第一个
将重复的数据删除
"""
kpil_df=salesdf.drop_duplicates(subset=["销售时间",'社保卡号'])

#总得消费次数：有多少行
total=kpil_df.shape[0]

print("总得消费次数：",total)

#月份数
starttime=kpil_df.loc[0,"销售时间"]
endtime=kpil_df.loc[total-1,'销售时间']
days=(endtime-starttime).days
month=days//30
print("月份数：",month)

#业务指标1：月平均消费次数=总次数/月数
kpi1=total/month
print("月平均消费次数：",kpi1)

#业务指标2：月平均消费额
#因为总得金额是包含同一时间和同一个社保卡号的，因此是不能用kpi_df,应该用去重之前的sale_df
totalmoney=salesdf.loc[:,"实收金额"].sum()
monthmoney=totalmoney/month
print("月平均消费额：",monthmoney)

#业务指标3：客单价
'''
总消费额/总次数
'''
pct=totalmoney/total
print("客单价：",pct)