# 定义集合
seta = {1,2}  # 空的一对大括弧定义的是字典，而不是集合
setnull = set()
print(seta)

# 集合是可变的
seta.add(8)
print(seta)

# 删集合元素
# seta.remove(9)
seta.discard(1)
print(seta)

# 集合的交际
setb = set(range(5))
print(seta & setb )

#
setb.update(list(range(5, 11)))
print(setb)