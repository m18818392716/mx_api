from django.db import models

# Create your models here.

class sign_event(models.Model):  # 必须继承models.Model
    # 不写则，django默认创建ID列，自增，主键
    # 用户名列，字符串类型，指定长度
    user_id = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    # amount = models.IntegerField
    # status = models.IntegerField(null=False)
    address = models.CharField(max_length=64)
    start_time = models.DateTimeField("%Y-%m-%d %H:%M:%S")

# python3 manage.py  makemigrations    # 生成migrations临时文件
# python3 manage.py  migrate           # 根据migrations直接生成数据库