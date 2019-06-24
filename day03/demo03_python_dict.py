# 定义词典
dict1 = {'no1' :{'name':'zhangsan', 'age' :20, 'sex' : 'male'}, 'no2':{'name' :'list', 'age' :30, 'sex' :'male'}}

# 访问字典，也是用类似数组下标索引的方式
print(dict1['no1'])
print(dict1['no1']['name'])

# 怎么来得到字典里所有的key
for key in dict1.keys():
    print(key)

# 怎样来得到所有的value
print(dict1.values())

# 通过get key来得到key对应的value
print(dict1.get('key'))

# items返回以key和value自称的一个元祖列表
print(dict1.items())

# updata
dict2 = {'no2' : 11111, 'no3' :22222}
dict1.update(dict2)
print(dict1)

# pop会删除元素而且会返回对应key的value
value = dict1.pop('no1')
print(value)
