# -*- coding:utf-8 -*-
# MongoDB基本使用
# pip install pymongo


from pymongo import  MongoClient
# 建立于MongoClient 的连接
client = MongoClient("localhost",27017)

# 得到数据库，只有插入数据时才会创建:
db = client.cache
# 或者
# db = client['cache']
print(db)

# 得到一个数据集合，只有插入数据时才会创建：
collection = db.test_collection
# 或者
# collection = db['test-collection']

# MongoDB中的数据使用的是类似Json风格的文档：
import datetime
post={
    "author":"Mike",
    "test":"My first blog post",
    "tags":["mongodb","python","pymongo"],
    "date":datetime.datetime.utcnow()

}
# 插入一个文档
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)