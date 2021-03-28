from scrapy import cmdline

if __name__ == '__main__':
    # 有色金属爬虫
    cmdline.execute("scrapy crawl Sci99Spider".split())

