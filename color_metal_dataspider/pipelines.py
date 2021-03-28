# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class ColorMetalDataspiderPipeline:

    def __init__(self):
        pass

    def process_item(self, item, spider):

        with open('../output/nm_sci99.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([item['name'], item['price'], item['change'], item['date']])

        return item