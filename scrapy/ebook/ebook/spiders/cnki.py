# -*- coding: utf-8 -*-
import scrapy
import re

class XzxzbSpider(scrapy.Spider):
    name = 'cnki'
    allowed_domains = ['cnki.net']
    start_urls = ['http://kns.cnki.net/']
    def parse(self, response):
        pages = response.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]/li')
        for page in pages:
            url = page.xpath('./child::a/attribute::href').extract_first()
            idx = page.xpath('./attribute::data-rid').extract_first()
            print(url)
            req = response.follow(url, callback=self.parse_chapter)
            req.meta['idx'] = idx
            yield req
        pass
    
