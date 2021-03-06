from scrapy import Selector
from scrapy.spiders import CrawlSpider
from ZKMasterInfo.items import ZkmasterinfoItem

from HashCode import getHashCode


class MasterInfo(CrawlSpider):
    name = "MasterInfo"  # 爬虫命名
    start_urls = ['http://blog.csdn.net/lmj623565791?viewmode=contents',
                  'http://blog.csdn.net/lfdfhl?viewmode=contents',
                  'http://blog.csdn.net/jdsjlzx?viewmode=contents',
                  'http://blog.csdn.net/lpjishu?viewmode=contents',
                  'http://blog.csdn.net/harvic880925?viewmode=contents',
                  'http://blog.csdn.net/iwanghang?viewmode=contents',
                  'http://blog.csdn.net/hejjunlin?viewmode=contents',
                  'http://blog.csdn.net/qq_26787115?viewmode=contents',
                  'http://blog.csdn.net/singwhatiwanna?viewmode=contents', ]  # 要爬取的页面地址

    def parse(self, response):
        print(response.body.decode('utf-8'))

        item = ZkmasterinfoItem()

        selector = Selector(response)

        name = selector.xpath('//span/a[@class="user_name"]/text()').extract()[0]  # 用户名
        nick_name = selector.xpath('//div[@id="blog_title"]/h2/a/text()').extract()[0]  # 昵称
        info = selector.xpath('//h3/text()').extract()[0]  # 用户名
        user_img = selector.xpath('//div[@id="blog_userface"]/a/img/@src').extract()[0]  # 用户图像
        blog = response.url  # 当前 url

        item['name'] = name
        item['nick_name'] = nick_name
        item['uid'] = getHashCode(response.url)
        item['img'] = user_img
        item['info'] = info
        item['isVip'] = '1'
        item['index'] = '11'
        item['blog'] = blog

        yield item
