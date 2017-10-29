# -*- coding: utf-8 -*-
import redis
class RedisOpera():

    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    def insert(self,url):
        self.r.sadd('svtcc_urls',url)

    def query(self,url):
        return self.r.sismember('svtcc_urls',url)