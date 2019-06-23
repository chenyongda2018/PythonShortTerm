#
# #定义
# def func_name():
#     pass
#
# func_name()
# #有一个参数的方法
# def func_name2(arg1):
#     pass
#
# func_name2(1)
# func_name2('str2')
#
# #有两个参数的方法
# def func_name3(arg1, arg2):
#     print(arg1, arg2)
#
# func_name3(10,'hello')

#默认参数
# def func_name4(arg1=10):
#     print(arg1)
#
#
# # func_name4(100)
# func_name4()


# def func_name5(a, b, c=10):
#     pass

# def func_name5(a, b=20, c):
#     pass

# def func_name5(a, b=20, c=30):
#     pass

# def func_name6(*arg):
#     print(arg)
#
# func_name6(1)
# func_name6(1,2)
# func_name6(1,2,3)


# def func(a=10, *args):
#     print(a)
#     print(args)

# func()
# func(1)
# func(1,2)
# func(1,2,3,4)

# def func_name7(a, **kwargs):
#     print(a)
#     print(kwargs)
#
#
# func_name7(10,name='Jack',age=10)



#默认返回值
# def func_name8():
#     x = 0
#
# result = func_name8()
# print(result)

def func_name9():
    return 1, 'str', [1, 2, 3, 4]

result = func_name9()
# print(result)
#
# a, b, c = func_name9()
# print(a)
# print(b)
# print(c)

a, _, _ = func_name9()
print(a)


