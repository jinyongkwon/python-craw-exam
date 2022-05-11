from pymongo import MongoClient
from pymongo.cursor import CursorType


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


list = []
dic = {
    "username": "ssar",
    "title": "1강"
}

dic2 = {
    "username": "cos",
    "title": "2강"
}

list.append(dic)
list.append(dic2)

# Mongo 연결
mongo = MongoClient("localhost", 20000)

a = mongo_save(mongo, list, "greendb", "test1")  # List안에 dict을 넣어야 함

print(a)
