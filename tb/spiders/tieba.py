# -*- coding: utf-8 -*-
import scrapy
import urllib
import json
import re



class TiebaSpider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/f?kw=%E6%A0%A1%E8%8A%B1&ie=utf-8&tab=good']


    def parse(self, response):
        href_list = re.findall('<a rel=\"noreferrer\" href="(.*?)" title=.*?</a>', response.body.decode())
        # next_url = response.xpath("//a[class='next pagination-item']/@href").extract_first()
        next_url = re.findall('<a href="(.*?)" class="next pagination-item " >', response.body.decode())[0]
        print(next_url)
        # print('*' * 100)
        # print(href_list)
        # print('*' * 100)
        for href in href_list:
            item = {}
            # item["title"] = []
            item["img_list"] = []
            item["video_list"] = []
            # item["content"] = []
            # item["author"] = []
            item["comment"] = []
            # item["publish_date"] = []
            if href is not None:
                href = urllib.parse.urljoin(response.url,href)
                item["href"] = href
                print(href)
                yield scrapy.Request(
                    href,
                    callback=self.parse_detail,
                    meta={"item":item},
                )

        if next_url is not None:#翻页
            next_url = urllib.parse.urljoin(response.url,next_url)
            # next_url = "https://tieba.baidu.com" + next_url[0]
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

            print('*' * 100)
            print("翻页")
            print('*' * 100)

        # yield (item)
    def parse_detail(self, response): #详情页获取数据
        item = response.meta["item"]
        # item["href"] = response.url
        item["title"] = response.xpath("//h1/text()").extract_first()
        item["img_list"].extend(response.xpath("//div/img/@src").extract())
        item["video_list"].extend(response.xpath("//div[@class='video_src_wrap_main']/video/@src").extract())
        item["content"] = response.xpath("/html/head/meta[2]/@content").extract_first()
        item["author"] = response.xpath("//div[@class='louzhubiaoshi  j_louzhubiaoshi']/@author").extract_first()
        item["comment"].extend(response.xpath("//div[@class='d_post_content j_d_post_content  clearfix']/text()").extract())
        item["publish_date"] = re.findall("(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2})",response.body.decode())[0]
        # item["publish_date"] = re.findall('&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tbclient&quot;,&quot;open_type&quot;:&quot;android&quot;,&quot;date&quot;:&quot;(.*?)&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:1,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:0,&quot;is_fold&quot;:0,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:0,&quot;pb_tpoint&quot;:null', response.body.decode())
        # if item["publish_date"] is None:
        #     item["publish_data"] = re.findall('&quot;is_anonym&quot;:false,&quot;open_id&quot;:&quot;tieba&quot;,&quot;open_type&quot;:&quot;&quot;,&quot;date&quot;:&quot;(.*?)&quot;,&quot;vote_crypt&quot;:&quot;&quot;,&quot;post_no&quot;:1,&quot;type&quot;:&quot;0&quot;,&quot;comment_num&quot;:0,&quot;is_fold&quot;:0,&quot;ptype&quot;:&quot;0&quot;,&quot;is_saveface&quot;:false,&quot;props&quot;:null,&quot;post_index&quot;:0,&quot;pb_tpoint&quot;:null',response.body.decode())
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        # yield item
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url, next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_detail,
                meta={"item": item}
            )
            # yield item
        else:
            yield item
            print(item)
        # yield item