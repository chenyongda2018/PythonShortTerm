# 运算符
print(2**10) # 求2的10次幂
print(10/3)
print(10//3) # //是求整数

# python没有 ++和 --
a = 1
b = 2

if a == 1 and b ==2
    pass
if a == 1 or b == 1
    pass
if not a == 1:
    pass

# in and not in
lista = list(range(10))
print(10 not in lista)

# is is not 对于不可变数据类型，重用内存
a = 1000000000000000000
b = 1000000000000000000
print(a is b)
del a
print(b)

lista = [1, 2, 3]
listb = [1, 2, 3]
print(lista is listb)
print(lista == listb)