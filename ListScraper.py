import urllib
from bs4 import BeautifulSoup
import requests
import scrapy

class StackSpider(scrapy.Spider):
    name = "metal-archives.com"
    # limit the scope to stackoverflow
    allowed_domains = ["metal-archives.com"]
    start_urls = [
        "https://www.metal-archives.com/label/index/l/C",
    ]

    def parse(self, response):
        hxs = scrapy.Selector(response)
        # extract all links from page
        for url in hxs.xpath('*//a/@href').extract():
            # make it a valid url
            if not ( url.startswith('http://') or url.startswith('https://') ):
                url = "https://www.metal-archives.com/label/index/l/C" + url
            # process the url
            self.handle(url)
            # recusively parse each url
            yield scrapy.http.Request(url=url, callback=self.parse)

    def handle(self, url):
        print(url)