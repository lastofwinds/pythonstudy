# import selectors
#
# '''
#     selectors模块：
#         与linux的epoll,还是select模块,poll等类似；实现高效的I/O 多路复用multiplexing，
#     常用于非阻塞的socket编程中，python官网文档也有介绍
# '''
#
# 1.模块定义了一个BaseSelectors抽象基类，以及子类：
#     SelectSelector
#     PollSelector
#     EpollSelector
#     DevpollSelector
#     KqueueSelector
#
#     另外还有一个DefaultSelector类，代理所有子类，也可以默认使用此类方法
#
# 2.模块定义了两个常量，用于描述Event Mask
#     EVENT_READ: 表示可读，值为1;
#     EVENT_WRITE: 表示可写，值为2;
#
# 3.模块定义了一个SelectoryKey类，一般用这个类的实例来描述一个已经注册的文件对象的状态，常用属性:
#     fileobj: 表示已经注册的文件对象;
#     fd: 表示文件对象的描述符，是一个整数，它是文件对象的fileno()方法的返回值;
#     events: 表示注册一个文件对象时，我们等待的events，Events Mask是可读还是可写;
#     data: 表示注册一个文件对象时绑定的data
#
# 4.一些抽象类方法:
#     register(fileobj,events,data=None)
#         注册一个对象:
#             fileobj:即可以是fd 也可以是一个拥有fileno()方法的对象;
#             events:上面events Mask常量；data
#         返回值：一个SelectorKey类的实例
#
#
#     unregister(fileobj)
#         注销一个对象:
#             ...
#
#     modify(fileobj,events,data=None)
#         修改一个已注册的文件对象:
#
#     select(timeout=None)
#         用于选择满足我们监听的event的文件对象;
#         返回值：(key,events)的元组;
#
#     close()
#         关闭selectors
#
#     get_key(fileobj)
#         返回文件对象的key;
#         返回值：一个SelectorKey类的实例;
#
#
