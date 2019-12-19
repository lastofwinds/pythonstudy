'''
    多进程同时获取数据，修改后重新赋值，可能同时拿到100，减一后把99赋值回去
得到的数据不准确，数据不安全可以通过加锁解决
'''
# from multiprocessing import Process,Manager
#
# def func(m_dic):
#     m_dic['count'] -= 1
#
# if __name__ == '__main__':
#     m = Manager()
#     m_dic = m.dict({'count': 100})
#     lst = []
#
#     for i in range(50):
#         p = Process(target=func,args=(m_dic,))
#         p.start()
#         lst.append(p)
#
#     [p.join() for p in lst]
#     print('主进程>>>',m_dic)



