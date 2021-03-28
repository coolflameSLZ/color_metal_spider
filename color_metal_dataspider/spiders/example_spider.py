import urllib

import scrapy


class ExampleSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://segmentfault.com/blog/sown',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response, **kwargs):
        for quote in response.css('section.stream-list__item'):
            title = quote.css('h2.title a::text').extract_first()
            article = urllib.parse.urljoin(response.url, quote.css('h2.title a::attr(href)').extract_first())

            # 继续解析。调用 parse_article·
            yield scrapy.Request(
                url=article,
                callback=self.parse_article,
                meta={'title': title}
            )

    def parse_article(self, response):
        title = response.meta['title']
        content = response.css('article.article').extract_first()
        # item = ArticleItem()
        # item['title'] = title
        # item['content'] = content
        # yield item
