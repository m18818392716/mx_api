#coding=utf-8
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
#如果给导入的模块起了别名，就必须使用别名，否则会出现错误。
#比如连接设备或模拟器，起了以上别名后，命令应该如下：
# device=mr.waitForConnection()

#参数1：超时时间，单位秒，浮点数。默认是无限期地等待。
#参数2：串deviceid，指定的设备名称。默认为当前设备（手机优先，比如手机通过USB线连接到PC、其次为模拟器）。
#默认连接：
device = mr.waitForConnection()
#参数连接：
device = mr.waitForConnection(5.0,'192.168.96.101:5555')
MonkeyRunner.sleep(5)
#device.startActivity(component="包名/启动Activity")
#以下两种都OK
device.startActivity(component="com.tnaot.news/com.tnaot.news.mctnews.detail.activity.MainActivity")
mr.sleep(10)
#获取设备的屏蔽缓冲区，产生了整个显示器的屏蔽捕获。（截图）
result=device.takeSnapshot()
#返回一个MonkeyImage对象（点阵图包装），我们可以用以下命令将图保存到文件
result.writeToFile('D:\Monkey\Test1_004.png','png')

#暂停目前正在运行的程序指定的秒数
#MonkeyRunner.sleep(秒数，浮点数)
mr.sleep(5)

# #device.type('字符串')
# device.type('Findyou')

# #锁屏后,屏幕关闭，可以用下命令唤醒
# device.wake()
# # 重启手机
# device.reboot()

#device.touch(x,y,触摸事件类型)
#x,y的单位为像素
#触摸事件类型，请见下文中Findyou对device.press描述
device.touch(1224,482,'DOWN_AND_UP')
mr.sleep(2)
device.touch(512,124,'DOWN_AND_UP')
MonkeyRunner.sleep(2)
device.type('测试')