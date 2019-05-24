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

class customer_userprofile(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
    lastLoginTime = models.CharField(max_length=32)
    id = models.CharField(max_length=32)
    baseCurrency = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)

class customer_overview(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)

    customer = models.CharField(max_length=32)

    name = models.CharField(max_length=32)
    account = models.CharField(max_length=32)
    currency = models.CharField(max_length=32)
    bookingCenter = models.CharField(max_length=32)
    updateDate = models.CharField(max_length=32)
    liabilitiesAmount = models.CharField(max_length=32)
    liabilitiesCurrency = models.CharField(max_length=32)
    netAssetsAmount = models.CharField(max_length=32)
    netAssetsCurrency = models.CharField(max_length=32)

    ytd = models.CharField(max_length=32)
    ytd_amount = models.CharField(max_length=32)
    ytd_currency = models.CharField(max_length=32)

    hasLiabilities = models.CharField(max_length=32)
    newDocumentCount = models.CharField(max_length=32)

class customer_accounts(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)

    accounts = models.CharField(max_length=32)

    id = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    weight = models.CharField(max_length=32)
    amount = models.CharField(max_length=32)
    externalId = models.CharField(max_length=32)
    currency = models.CharField(max_length=32)
    baseCurrency = models.CharField(max_length=32)

    totalSize = models.CharField(max_length=32)

class customer_allocation(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)

    clazz = models.CharField(max_length=32)

    clazz_id = models.CharField(max_length=32)
    clazz_amount = models.CharField(max_length=32)
    clazz_name = models.CharField(max_length=32)
    clazz_weight = models.CharField(max_length=32)
    clazz_currency = models.CharField(max_length=32)
    clazz_nodes = models.CharField(max_length=32)
    clazz_nodes_id = models.CharField(max_length=32)
    clazz_nodes_amount = models.CharField(max_length=32)
    clazz_nodes_name = models.CharField(max_length=32)
    clazz_nodes_currency = models.CharField(max_length=32)
    clazz_nodes_weight = models.CharField(max_length=32)
    clazz_donutWeight = models.CharField(max_length=32)

    currency = models.CharField(max_length=32)

    currency_id = models.CharField(max_length=32)
    currency_amount = models.CharField(max_length=32)
    currency_name = models.CharField(max_length=32)
    currency_currency = models.CharField(max_length=32)
    currency_donutWeight = models.CharField(max_length=32)

    region = models.CharField(max_length=32)

    region_id = models.CharField(max_length=32)
    region_amount = models.CharField(max_length=32)
    region_name = models.CharField(max_length=32)
    region_currency = models.CharField(max_length=32)
    region_weight = models.CharField(max_length=32)
    region_donutWeight = models.CharField(max_length=32)

class customer_rate(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
    lastLoginTime = models.CharField(max_length=32)
    id = models.CharField(max_length=32)
    baseCurrency = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)

class customer_allocation_holdings(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
    lastLoginTime = models.CharField(max_length=32)
    id = models.CharField(max_length=32)
    baseCurrency = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)

class customer_allocation_holding_group(models.Model):
    code = models.CharField(max_length=32)
    message = models.CharField(max_length=32)
    data = models.CharField(max_length=32)
    lastLoginTime = models.CharField(max_length=32)
    id = models.CharField(max_length=32)
    baseCurrency = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)