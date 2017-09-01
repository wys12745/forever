# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector,Selector
from scrapy.http import Request

class XiaohuarSpider(scrapy.Spider):
    name = 'xiaohuar'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/hua/']

    def parse(self, response):
        # 要废弃(不要使用这种)
        # hxs = HtmlXPathSelector(response)
        # result = hxs.select('//a[@class="item_list"]')

        #使用下面这种
        hxs = Selector(response=response)

        user_list = hxs.xpath('//div[@class="item masonry_brick"]')
        for item in user_list:
            price = item.xpath('.//span[@class="price"]/text()').extract_first()
            url = item.xpath('div[@class="item_t"]/div[@class="class"]//a/@href').extract_first()
            print(price,url)

        result = hxs.xpath('/a[re:test(@href,"http://www.xiaohuar.com/list-1-\d+.html")]/@href')
        print(result)
        result = ['http://www.xiaohuar.com/list-1-1.html','http://www.xiaohuar.com/list-1-2.html']

        # 规则
        for url in result:
            yield Request(url=url,callback=self.parse)

