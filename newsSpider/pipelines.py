# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from redis_cls import RedisOpera
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
import MySQLdb

class NewsspiderPipeline(object):


    def __init__(self):
        self.redis = RedisOpera()


    def process_item(self, item, spider):
        self.redis.insert(item['url'])
        conn = MySQLdb.connect("localhost", "root", "root", "news",charset="utf8")
        cur = conn.cursor()
        sql = "insert into svtcc_news (`title`,`date`,`content`,`author`,`url`) VALUES ('%s','%s','%s','%s','%s')" \
              %(item['title'],item['date'].decode('utf-8'),item['content'],item['author'].decode('utf-8'),item['url'])
        try:
            # 执行sql语句
            cur.execute(sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # Rollback in case there is any error
            conn.rollback()
        conn.close()
        # print item['title']
        return item
