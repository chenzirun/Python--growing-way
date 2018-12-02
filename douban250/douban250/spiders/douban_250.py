# -*- coding: utf-8 -*-
import scrapy
from douban250.items import Douban250Item


class Douban250Spider(scrapy.Spider):
    name = 'douban_250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_lis = response.css('ol.grid_view div.info')
        for movie_li in movie_lis:
            item = Douban250Item()

            item['name'] = movie_li.css('.hd a span:nth-child(1)::text').extract_first()
            item['link'] = movie_li.css('.hd a::attr("href")').extract_first()
            item['comment'] = movie_li.css('span.inq::text').extract_first()

            yield item


        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if next_page is not None:
            next_page = 'https://movie.douban.com/top250' + next_page
            yield scrapy.Request(next_page, callback=self.parse)
