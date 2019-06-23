# -*- coding:utf-8 -*-
# 插入多条记录
from pymongo import MongoClient


import datetime
import copy
post={
    "author":"Mike",
    "test":"My first blog post",
    "tags":["mongodb","python","pymongo"],
    "date":datetime.datetime.utcnow()

}

client = MongoClient("localhost",27017)
db = client.cache2
posts = db.posts

# for i in range(10):
#     p= copy.copy(post)
#     # 会修改原来的post
#     posts.insert(p)
#
#
#
# for p in posts.find():
#     print(p)


for p in posts.find({'author':'Mike'}):
    print(p)



