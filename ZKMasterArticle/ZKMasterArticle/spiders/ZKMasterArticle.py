from scrapy import Selector
from scrapy.spiders import CrawlSpider

from ZKMasterArticle.items import ZkmasterarticleItem


class ZKMasterArticle(CrawlSpider):
    name = "ZKMasterArticle"  # 爬虫命名
    start_urls = ['http://blog.csdn.net/singwhatiwanna?viewmode=contents']  # 要爬取的页面地址

    def parse(self, response):
        print(response.body.decode('utf-8'))

        selector = Selector(response)

        csdn_name = selector.xpath('//span/a[@class="user_name"]/text()').extract()[0]  # 用户名
        address = selector.xpath('//span[@class="link_title"]/a/@href').extract()  # 地址
        blog_list = selector.xpath('//span[@class="link_title"]/a/text()').extract()  # 博客目录
        des = selector.xpath('//div[@id="blog_title"]/h3/text()').extract()[0]  # 博主描述

        print(csdn_name)

        for i in range(len(address)):
            item = ZkmasterarticleItem()
            item['uid'] = '10001'
            item['des'] = des
            item['article_title'] = blog_list[i + 1].strip()
            item['article_address'] = 'http://blog.csdn.net' + address[i]
            yield item