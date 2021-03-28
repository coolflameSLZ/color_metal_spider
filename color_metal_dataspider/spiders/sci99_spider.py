# 引入文件
import scrapy


class Sci99Spider(scrapy.Spider):
    # 用于区别Spider
    name = "Sci99Spider"

    # 爬取的地址
    def start_requests(self):
        urls = [
            'https://nm.sci99.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    # 爬取方法
    def parse(self, response, **kwargs):
        from color_metal_dataspider.items import ColorMetalItem

        item = ColorMetalItem()

        for box in response.css('.tab_spas tr')[1:]:
            # print("=====", box.extract())
            name = box.xpath('.//th/a/text()').extract()[0].strip()
            price = box.xpath('.//td[1]/text()').extract()[0].strip()
            change = box.xpath('.//td[2]/span/text()').extract()[0].strip()
            date = box.xpath('.//td[3]/text()').extract()[0].strip()
            # print(name, price, change, date)
            item['name'] = name
            item['price'] = price
            item['change'] = change
            item['date'] = date

            yield item

    pass
