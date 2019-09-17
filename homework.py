#第一题:请问如何修改以下Python代码，使下面的代码调用类A的show方法？
# class A(object):
#     def show(self):
#         print('base show')
#
# class B(A):
#     def show(self):
#         print('derived show')
#         super().show()
#
# obj=B()
# obj.show()

#第二题：请问如何修改以下Python代码，使得代码能够运行？
# class A(object):
#     def __init__(self,a,b=None):
#         self.__a=a
#         self.__b=b
#     def myprint(self):
#         print('a=',self.__a,'b',self.__b)
#
# a1=A(10,20)
# a1.myprint()
# a1.__init__(80)
# a1.myprint()

#第三题：求下面代码输出什么
#a1:B fn
"""
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例对象，是个静态方法。
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值，通常用在初始化一个类实例的时候。是一个实例方法。
也就是： __new__先被调用，__init__后被调用，__new__的返回值（实例）将传递给__init__方法的第一个参数，然后__init__给这个实例设置一些参数。
"""

# #第四题:
# ls=[1,2,3,4]
# list1=[i for i in ls if i >2]
# print(list1)#[3,4]
#
# list2=[i*2 for i in ls if i>2]
# print(list2)#[6,8]
#
# dic1={x:x**2 for x in (2,4,6)}
# print(dic1)#{2:4,4:16,6:36}
#
# set1={x for x in 'hello world' if x not in 'low level'}
# print(set1)#{h r d}

#第五题:
#f2(): 9
#f1(): 没有输出 因为无返回值
#f2(): 9 #全局变量
# num=9
# def f1():
#     num=20
# def f2():
#     print(num)
# f2()
# f1()
# f2()

#第六题：
# class A(object):
#     def __init__(self,a,b):
#         self.a1=a
#         self.b1=b
#         print('init')
#
#     def mydefault(self,func):
#         def wrapper(*args,**kwargs):
#             print('内部返回值')
#             func(*args,kwargs)
#         return wrapper
#     @mydefault
#     def fn1(self):
#         print('第二个函数')
# a1=A(10,20)
# a1.fn1()
# a1.fn2()
# a1.fn3()

def print_func(func):
    def wrapper(*args,**kwargs):
        print('拦截')
        func(*args,**kwargs)
    return wrapper
@print_func
def fun(a,b):
    print('你好阿',a,b)
fun(45,78)