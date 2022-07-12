import scrapy
import os
import urllib.parse

class CatsUrlsSpider(scrapy.Spider):
    name = 'cats_urls'
    allowed_domains = ['www.joesnewbalanceoutlet.com']
    start_urls = ['http://www.joesnewbalanceoutlet.com/']

    def start_requests(self):
        url = self.start_urls[0]
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        urls = response.css('[title="View All"]::attr(href)').getall()
        cats_urls = [urllib.parse.urljoin( self.start_urls[0] , url) for url in urls]
        for url in cats_urls:
            yield  {'urls':url}
