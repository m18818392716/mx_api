from configparser import ConfigParser

# 初始化类
cp = ConfigParser()
cp.read("../dataconfig/request_config.ini")


# 得到[request_host]
host_section = cp.sections()[0]
# 得到[request_header]
header_section = cp.sections()[1]


def get_header(key=None):
    if key:
        # 获取指定header
        return cp.get(header_section, key)
    else:
        # 获取所有header
        return dict(cp.items(header_section))


def set_header(key, value):
    cp.set(header_section, key, value)


# 获取host
def get_host():
    return cp.get(host_section, 'host')

# print(get_header())
# print(get_host())
