# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy import FormRequest

from newsSpider.items import NewsspiderItem


class SvtccSpider(scrapy.Spider):

    name = 'svtcc_spider'
    allowed_domains = ["news.svtcc.edu.cn"]

    def __init__(self):
        self.archive_re = re.compile(r'http://news.svtcc.edu.cn/index.php/archive/.+?\.html')


    def start_requests(self):
        yield FormRequest('http://news.svtcc.edu.cn/',callback=self.parse)

    def parse(self, response):
        select_a =  response.css("a")
        for tag_a in select_a:
            url = tag_a.css("::attr(href)").extract()
            if len(url) > 0:
                url = url[0].strip()
                if len(url) == 0: url = None
            else:
                url = None
            if url:
                if self.archive_re.match(url):
                    yield FormRequest(url,callback=self.archive)
                else:
                    yield FormRequest(url,callback=self.parse)



    def archive(self,response):
        title_tag = response.css('.noBorder::text').extract_first().strip()
        art_author = response.css('.art_author::text').extract_first().strip()
        art_authors = art_author.encode('utf-8').split("：")
        if len(art_authors) == 2:
            art_author = art_authors[1]
        else:
            art_author = u'佚名'
        art_publish = response.css('.art_publish::text').extract_first().strip()
        art_publishs = art_publish.encode('utf-8').split("：")
        if len(art_publishs) == 2:
            art_publish = art_publishs[1]
        else:
            art_publish = '2001-01-01'
        art_con = response.css('.atr_con').extract_first()
        item = NewsspiderItem()
        item['title'] = title_tag
        item['author'] = art_author
        item['date'] = art_publish
        item['content'] = art_con
        item['url'] = response.url
        # print item['title']
        yield item
