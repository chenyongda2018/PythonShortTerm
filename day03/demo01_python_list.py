# 定义list
lista = [1, 'xiaojiejie', 20, 'female']
print(type(lista))
print(lista)

# 遍历列表
for element in lista:
    print(element)
    pass

# 下标取列表元素
    print(lista[1])

# 使用range来生成list
listb = list(range(10))
print(listb)
# 生成0到10的偶数
listc = list(range(0, 10, 2))
print(listc)
print(range(10))

# list切片
listd = list(range(20))
print(listd)
print(listd[0:10])
print(listd[0:20:2])

# list是可变数据类型
listd.append(20)
print(listd)
listd.insert(5, 20000)
print(listd)
listd.remove(listd[5])
print(listd)

# + *
print(listd+listd)
print(listd * 10)

# list嵌套
liste = [1, 2, 3, 4, 5]
liste.append(list(range(6, 11)))
print(liste)
print(liste[5][0])

# 打散插入
listf = list("abcdefg")
print(listf)

print(len(listf))
print(max(listf))
print(min(liste))

# list排序
listg = [4, 1, 2, 6, 3, 5, 0]
listg.reverse()
print(listg)
listg.sort(reverse = True)
print(listg)

# [:]深复制
listh = list(range(20))
listi = listh
listi[0] = 200
print(listh)

listj = listh[:] # 深复制
listj[0] = 20000
print(listj)
print(listh)