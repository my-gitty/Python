# -*- coding: utf-8 -*-
import scrapy
import re

class XzxzbSpider(scrapy.Spider):
    name = 'xzxzb'
    allowed_domains = ['qidian.com']
    start_urls = ['https://book.qidian.com/info/1010780117/']
    def parse(self, response):
        pages = response.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]/li')
        for page in pages:
            url = page.xpath('./child::a/attribute::href').extract_first()
            idx = page.xpath('./attribute::data-rid').extract_first()
            # yield scrapy.Request('https:' + url, callback=self.parse_chapter)
            req = response.follow(url, callback=self.parse_chapter)
            req.meta['idx'] = idx
            yield req
        pass
    def parse_chapter(self, response):
        idx = response.meta['idx']
        title = response.xpath('//div[@class="main-text-wrap"]//h3[@class="j_chapterName"]/text()').extract_first().strip()
        content = response.xpath('//div[@class="main-text-wrap"]//div[@class="read-content j_readContent"]').extract_first().strip()
        # print title
        # print content
        # content = re.sub('</?p>', '\n', content)
        p = re.compile('<[^>]+>')
        content = p.sub("\n", content)
        filename = './down/%s_%s.txt' % (idx, title)
        cnt = '\n%s\n%s' % (title, content)
        
        # cnt.replace(r'</p>', '\n')
        # print(cnt)
        with open('./down/1.txt', 'ab+') as f:
            f.write(cnt.encode('utf-8'))
        pass
