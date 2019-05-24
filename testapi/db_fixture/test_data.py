# coding:utf-8

from testapi.config.readDbConfig import DB

# 创建测试数据
datas = {
    # 发布会表数据
    "testapi_sign_event": [
        {"user_id": 1, "name": "红米Pro发布会", "address": "北京会展中心",
         "start_time": "2018-10-31 08:00:00"},
        {"user_id": 2, "name": "可参加人数为0", "address": "北京会展中心",
         "start_time": "2018-10-31 08:00:00"},
        {"user_id": 3, "name": "当前状态为0关闭", "address": "北京会展中心",
         "start_time": "2018-10-31 08:00:00"},
        {"user_id": 4, "name": "发布会已结束", "address": "北京会展中心",
         "start_time": "2017-10-31 08:00:00"},
        {"user_id": 5, "name": "小米5发布会", "address": "北京会展中心",
         "start_time": "2018-10-31 08:00:00"}
    ]
}


# 将测试数据插入表
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()


if __name__ == '__main__':
    init_data()