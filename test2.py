from turtle import title
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_one(datas).inserted_ids
    return result


now = datetime.now()

html = requests.get(
    f"https://n.news.naver.com/mnews/article/005/0000000005?sid=100")
soup = BeautifulSoup(html.text, 'html.parser')
if(html.status_code == 200):
    company = soup.select_one('meta[name="twitter:creator"]')['content']
    title = soup.select_one(".end_tit").get_text()  # 태그 제거
    dic = {
        "company": company,
        "title": title.strip('\n\t\t\t'),  # \n 제거
        # formatter => 원하는 날짜 형식으로 가져옴.
        "createAt": now.strftime('%Y년%m월%d일 %H시%M분%S초')
    }
    print(dic)
    # mongo = MongoClient("localhost", 20000)
    # mongo_save(mongo, dic, "greendb", "test")  # List안에 dict을 넣어야 함
