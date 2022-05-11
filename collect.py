import requests
from datetime import datetime
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.cursor import CursorType


def mongo_save(mongo, datas, db_name=None, collection_name=None):
    result = mongo[db_name][collection_name].insert_many(datas).inserted_ids
    return result


list = []
now = datetime.now()
aid = 1
while True:
    format_aid = '{0:010d}'.format(aid)
    html = requests.get(
        f"https://n.news.naver.com/mnews/article/005/{format_aid}?sid=100")
    soup = BeautifulSoup(html.text, 'html.parser')
    if(html.status_code == 200):
        company = soup.select_one('meta[name="twitter:creator"]')['content']
        title = soup.select_one(".media_end_head_headline")
        if title != None:
            title = title.get_text()
            dic = {
                "company": company,
                "title": title.strip('\n\t\t\t'),  # \n 제거
                # formatter => 원하는 날짜 형식으로 가져옴.
                "createAt": now.strftime('%Y년%m월%d일 %H시%M분%S초')
            }
            list.append(dic)
    aid += 1
    if len(list) == 20:
        break

mongo = MongoClient("localhost", 20000)
mongo_save(mongo, list, "greendb", "navers")
