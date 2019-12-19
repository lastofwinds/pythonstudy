
'''加锁，解决数据错乱问题'''
# from multiprocessing import Process,Manager,Lock
#
# def func(m_dic,ml):
#     with ml:
#         m_dic['count'] -= 1
#
# if __name__ == '__main__':
#     m = Manager()
#     ml = Lock()
#     m_dic = m.dict({'count': 100})
#
#     lst = []
#     for i in range(50):
#         p = Process(target=func,args=(m_dic,ml))
#         p.start()
#
#         lst.append(p)
#
#     [p.join() for p in lst]
#     print(m_dic)

