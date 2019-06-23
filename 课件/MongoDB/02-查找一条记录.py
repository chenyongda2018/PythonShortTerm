# -*- coding:utf-8 -*-
# 查找一条数据
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("localhost",27017)
db = client.cache
posts = db.posts
print posts.find_one()

# 条件查找
print posts.find_one({'author':'Mike'})
# 通过ObjectID查找
ID = posts.find_one()['_id']
print(ID)
print(type(ID))

print posts.find_one({'_id':ID})
print posts.find_one({'_id':ObjectId(ID)})

# 不要转化ObjectID为String
post_id_as_str = str(ID)
print posts.find_one({"_id":post_id_as_str})
