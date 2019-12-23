'''
    一个greenlet 是一个小型的独立伪线程，相当于在线程中使用的更小单元，在更小单元中，
有多个小单元中在处理数据，在线程的管理下，一个greenlet必须选择跳转到另一个greenlet，
这会让前一个挂起，而后一个在此前挂起处恢复执行，不同的greenlet之间的跳转成为切换(switching)
    当你创建一个greenlet时，它得到一个开始时为空的栈，当你第一次切换到它时，它会执行指定的
函数，这个函数可能会调用其他函数/切换跳其他greenlet，当最终栈底函数执行结束出栈时，这个greenlet
的栈又变成空的，这个greenlet也就死掉了，greenlet也会因为一个未捕捉的异常死掉。
'''
#
# import greenlet
# from greenlet import greenlet
# import gevent
# import time
#
# def eat(name):
#     print('%s eat 1' % name)
#     time.sleep(1)
#     g2.switch('taibai')
#     print('%s eat 2' % name)
#     g2.switch()
#
#
# def play(name):
#     print('%s play 1' % name)
#     g1.switch()
#     print('%s play 2' % name)
#
# g1 = greenlet(eat)
# g2 = greenlet(play)
#
# g1.switch('taibai')  #可以在第一次switch时传入参数，以后都不需要
#
#
#
#
#
