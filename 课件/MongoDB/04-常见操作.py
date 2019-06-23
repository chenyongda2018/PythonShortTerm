# -*- coding:utf-8 -*-
# 聚集操作

from pymongo import MongoClient,ASCENDING,DESCENDING

client = MongoClient("localhost",27017)
db = client.cache2
# 获得所有聚集名称
print db.collection_names()



# 查看聚集的一条记录
print db.posts.find_one()
print db.posts.find_one({'author':'Mike'})

# 查看聚集的字段
print db.posts.find_one({},{"author":'Mike'})

# 聚集查询结果排序
db.posts.find().sort('author')#默认为升序
db.posts.find().sort('author',ASCENDING)#升序

db.posts.find().sort('author',DESCENDING)#降序

# 修改一条记录
# db.collection.update( criteria, objNew, upsert, multi )
    # criteria : update的查询条件，类似sql update查询内where后面的
    # objNew   : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
    # upsert   : 这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
    # multi    : mongodb默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
db.posts.update({'author':'Mike'}, {'$set':{'author':'Jack'}},multi=True)


#另一种方式
doc = db.posts.find_one({'author':'Mike'})
print type(doc)
print doc['author']
doc['author'] = 'Tonny'
db.posts.save(doc)


# 按条件删除
db.posts.remove({'author':'tom'})
# # 删除全部记录
db.posts.remove()




posts = db.posts
# 获取集合的数据条数
print posts.count()
# 满足某种查找条件的数据条数：
print posts.find({'author':'Mike'}).count()
# 范围查找，比如说时间范围
d = datetime.datetime(2009, 11, 12, 12)
print '----------------------------小于该日期------------------------------'
for p in posts.find({"date": {"$lt": d}}).sort("author"):
    print(p)
print '----------------------------大于该日期------------------------------'
for p in posts.find({"date": {"$gt": d}}).sort("author"):
    print(p)
    
