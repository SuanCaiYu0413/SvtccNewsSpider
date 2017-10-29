# 四川交通职业技术学院新闻网增量爬虫

- 采用Scrapy框架编写，将爬取过的链接存放在redis中，在pipelines中添加已经爬取过的url，在middlewares中查看url是否已经爬取过。
- 爬取的数据存放与Mysql中



## 运行环境

- Python 2.7.x
- Scrapy 1.4.0
- redis 2.10.6
- MySQLdb 1.2.5