import scrapy
import sys
import json
import csv

class SneakersSpider(scrapy.Spider):
    name = 'sneakers'

    def start_requests(self):
        products_urls = []
        with open("products.csv", 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                products_urls.append(row[0])

        for url in products_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'name'  :response.css('[itemprop="name"]::text').get(),
            'price' :response.css('[itemprop="price"]::text').get(),
            'description' :response.css('[itemprop="description"]::text').get()
        }

