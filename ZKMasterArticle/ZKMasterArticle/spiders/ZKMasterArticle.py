from scrapy import Selector
from scrapy.spiders import CrawlSpider
from HashCode import getHashCode
from ZKMasterArticle.items import ZkmasterarticleItem


class ZKMasterArticle(CrawlSpider):
    name = "ZKMasterArticle"  # 爬虫命名
    start_urls = ['http://blog.csdn.net/lmj623565791?viewmode=contents',
                  'http://blog.csdn.net/lfdfhl?viewmode=contents',
                  'http://blog.csdn.net/jdsjlzx?viewmode=contents',
                  'http://blog.csdn.net/lpjishu?viewmode=contents',
                  'http://blog.csdn.net/harvic880925?viewmode=contents',
                  'http://blog.csdn.net/iwanghang?viewmode=contents',
                  'http://blog.csdn.net/hejjunlin?viewmode=contents',
                  'http://blog.csdn.net/qq_26787115?viewmode=contents',
                  'http://blog.csdn.net/singwhatiwanna?viewmode=contents',]  # 要爬取的页面地址

    def parse(self, response):
        print(response.body.decode('utf-8'))

        selector = Selector(response)

        name = selector.xpath('//span/a[@class="user_name"]/text()').extract()[0]  # 用户名
        nick_name = selector.xpath('//div[@id="blog_title"]/h2/a/text()').extract()[0]  # 昵称
        address = selector.xpath('//span[@class="link_title"]/a/@href').extract()  # 地址
        blog_list = selector.xpath('//span[@class="link_title"]/a/text()').extract()  # 博客目录
        des = selector.xpath('//div[@id="blog_title"]/h3/text()').extract()[0]  # 博主描述

        print(name)

        for i in range(len(address)):
            item = ZkmasterarticleItem()
            item['uid'] = getHashCode(response.url)
            item['name'] = name
            item['nick_name'] = nick_name
            item['des'] = des
            item['article_title'] = blog_list[i + 1].strip()
            item['article_address'] = 'http://blog.csdn.net' + address[i]
            yield item
