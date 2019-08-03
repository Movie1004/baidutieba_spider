# -*- coding: utf-8 -*-
import scrapy


class TestUaSpider(scrapy.Spider):
    name = 'test_ua'
    # allowed_domains = ['baidu.com']
    # start_urls = ['http://baidu.com/']


    def __init__(self):
        self.test_url = 'http://httpbin.org/get'


    def start_requests(self):
        yield scrapy.Request(
            self.test_url,
            callback=self.parse,
        )

    def parse(self,response):
        print('\n')
        print(response.request.headers["User-Agent"],'\n')
        print(response.text)


