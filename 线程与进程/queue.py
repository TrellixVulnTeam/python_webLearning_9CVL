#coding:utf-8
from multiprocessing import Queue
q = Queue(3) # 初始化一个queue队列  最大线程数3
q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

#因为消息队列已满的下面的try都会跑出一个异常，第一饿try会等待2秒后再抛出异常，第二个会立即抛出
# try:
# 	q.put("消息4",True,2)
# except:
#     print("消息队列已满，现有消息数量:%s"%q.qsize())


# try:
# 	q.put_nowait("消息4")
# except:
#     print("消息队列已满，现有纤细数量:%s"%q.qsize())



#推荐写法
print("="*30)
if not q.full():
	q.put_nowait("消息4")


#读取消息 先判断消息队列是否为空  再读取
if not q.empty():
	for i in range(q.qsize()):
		print(q.get_nowait())