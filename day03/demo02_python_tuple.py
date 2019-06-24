# ()定义tuple
tuple1 = (1,  'zhangsan', 20, 100000.00)

# 遍历tuple
for t in tuple1:
    print(t)
# tuple定义完成之后就不能变了
print(tuple[0])
# tuple1[0] = 2 错误


# 其他的tuple定义方式
tuple2 = tuple('abcdefg')
print(tuple2)

print(tuple2[:])

# 特别说明：如何定义只要一个元素的tuple
lista = [1]
tuple3 = (1)  # 这个定义不能构成tuple
print(type(tuple3))
tuple4 = (1,)
print(type(tuple4))

print(tuple4.count(1))
print(tuple4.index(1))

# tuple也是可以嵌套的
tuple5 = ((1, 'xiaojiejie', 18), (2, 'xiaogege', 20), (3, 'wangwu', 40))
print(tuple5[1][1])