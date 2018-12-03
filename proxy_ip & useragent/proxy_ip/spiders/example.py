# -*- coding: utf-8 -*-
import scrapy
from proxy_ip.items import ProxyIpItem


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['kuaidaili.com']
    #start_urls = ['http://kuaidaili.com/']

    def start_requests(self):
        start_urls = []
        for i in range(1, 10):
            url = scrapy.Request(f'https://www.kuaidaili.com/free/intr/{i}/', callback=self.parse)
            start_urls.append(url)

        return  start_urls

    def parse(self, response):
        ip_data = response.xpath('//tbody')
        trs = ip_data[0].xpath('tr')

        for ip in trs:
            item = ProxyIpItem()

            item['IP'] = ip.xpath('td[1]/text()').extract_first()
            item['PORT'] =  ip.xpath('td[2]/text()').extract_first()
            item['POSITION'] = ip.xpath('td[5]/text()').extract_first()
            item['TYPE'] = ip.xpath('td[4]/text()').extract_first()
            item['SPEED'] = ip.xpath('td[6]/text()').extract_first()
            item['LAST_CHECK_TIME'] = ip.xpath('td[7]/text()').extract_first()

            yield item


