##基本数据类型
a, b, c, d = 1, 2.0, True, "hello"
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 列表 list
list1 = ['a', 'b', 'c']
list2 = ['d', 'e', 'f']
print(list1 + list2)
print(list1[0:2])  # a,b
print(list2[-1])  # ｆ

# 步长
list3 = [1, 2, 3, 4, 5, 6]
print(list3[0:5:2])

# 元祖
tuple = (1, 2, 3, 4, 5)
# tuple[0] = 2
# print(tuple)  # 这里会报错，以为元祖的元素不能更改


# set集合 会自动去重
set1 = {1, 2, 3, 4, 5, 6, 6}
print(set1)  # 1,2,3,4,5

# dict 字典
dict1 = {x: x * 2 for x in (2, 4, 6)}
print(dict1)

