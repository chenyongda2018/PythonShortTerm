#HashMap HashTable
#dict
dict_1 ={}
print(type(dict_1))
#键 - 值   对
dict_2 = {'name':'Jack'}
print(dict_2)

dict_3 =  {'age': 10,
           'name':'Jack',
           'gender':'male'
}
# print(dict_3)
# print(dict_3['name'])
# print(dict_3['age'])
# dict_3['name'] = '小明'
# print(dict_3)
# print(dict_3['id'])
# print(dict_3.get('id',1))

# print( 'age' in dict_3)
# print( 'id' in dict_3)

# print(dict_3)
# dict_3.pop('name')
# # del dict_3['name']
# print(dict_3)
#
# dict_3['height'] =170
# print(dict_3)

#HashSet
#set
#
# my_set = set({1, 2, 1, 3, 4})
# print(type(my_set))
# print(my_set)
#
# my_set.add('Jack')
# print(my_set)
#
# my_set.add('Tom')
# print(my_set)
#
# my_set.remove(2)
# print(my_set)

s1 = set({1, 2, 3})
s2 = {3, 4, 5}
print(s1, s2)
print(type(s1),type(s2))
s3 = s1 | s2
print(s3)

s4 = s1 & s2
print(s4)
