# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings




class TbPipeline(object):
    def __init__(self):
        # 获取setting主机名、端口号和数据库名称
        settings = get_project_settings()
        host = settings.get('MONGODB_HOST')
        port = settings.get('MONGODB_PORT')
        dbname = settings.get('MONGODB_DBNAME')

        # 创建数据库连接
        client = MongoClient(host=host,port=port)

        # 指向指定数据库
        mdb = client['Tieba']

        # 获取数据库里面存放数据的表名
        self.post = mdb[settings.get('MONGODB_DOCNAME')]

    def process_item(self, item, spider):
        if spider.name == 'tieba':
            data = dict(item)
            # 向指定的表里添加数据
            self.post.insert(data)
            return item
        # NewsDB.new.update(spec, {"$set": dict(item)}, upsert=True)
        # return None
        # data = dict(item)
        # # 向指定的表里添加数据
        # self.post.insert(data)
        # return item
        # print(item)
        # collection.insert(item)
        # return item
