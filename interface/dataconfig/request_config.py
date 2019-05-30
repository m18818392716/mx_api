from configparser import ConfigParser

# 初始化类
cp = ConfigParser()
cp.read("../dataconfig/request_config.ini")

# 得到[request_header]
section = cp.sections()[0]


def get_header(key=None):
    if key:
        # 获取指定header
        return cp.get(section, key)
    else:
        # 获取所有header
        return dict(cp.items(section))


def set_header(key, value):
    cp.set(section, key, value)


print(get_header())
