import scrapy
import json
import sys
from pprint import pprint
import urllib.parse
import csv

class ProductsUrlsSpider(scrapy.Spider):
    name = 'products_urls'
    allowed_domains = ['www.joesnewbalanceoutlet.com']
    start_urls = ['http://www.joesnewbalanceoutlet.com/']

    def start_requests(self):
        # with open('cats.json') as json_file:
            # data = json.load(json_file)

        cats_urls = []
        with open("cats.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                cats_urls.append(row[0])

        # sys.exit()
        # cats_urls = data[0]['urls']
        for cat_url in cats_urls:
            url = cat_url + '?PageSize=60'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = response.css('.figureWrapper > a[data-productname]::attr(href)').getall()
        products_urls = [urllib.parse.urljoin( self.start_urls[0] , url) for url in urls]
        for url in products_urls:
            yield  {'urls':url}

        next_page = response.css('.pagingNext::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
