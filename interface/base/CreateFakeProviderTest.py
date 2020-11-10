# -*- coding: utf-8 -*-
__author__ = "苦叶子"
"""
    实现一个简单的faker provider
"""
from faker import Faker

# 从providers中导入internet组件
from faker.providers import internet

# 导入provider基类，我们的provider需要继承该类
from faker.providers import BaseProvider


# 创建一个我们的provider
class MyProvider(BaseProvider):
    def my_name(self):
        return "DeepTest"
if __name__ == "__main__":
    print("使用自定义Provider实例")

    fake = Faker('zh_CN')

    # 将自定义provider添加至fake
    fake.add_provider(MyProvider)
    fake.add_provider(internet)

    # 调用自定义provider中方法，生成数据
    my_name = fake.my_name()

    # 生成一个私有的ip
    ip = fake.ipv4_private()

print(my_name)
print(ip)
print('生成Python字典: {}'.format(fake.pydict(
        nb_elements=10, variable_nb_elements=True)))  # Python字典
print('生成Python可迭代对象:{}.'.format(fake.pyiterable(
        nb_elements=10, variable_nb_elements=True)))  # Python可迭代对象
print('生成Python结构：{}'.format(fake.pystruct(count=1)))  # Python结构

print(fake.profile()) #生成个人档案信息