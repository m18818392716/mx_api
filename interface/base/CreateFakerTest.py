from faker import Faker

fake = Faker(locale='zh_CN')
for _ in range(5):
    print('姓名：', fake.name(), ' 手机号：', fake.phone_number())
fake.random.getstate()

for _ in range(3):
     # Raises a UniquenessException
     fake.unique.boolean()