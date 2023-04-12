# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class LagouItem(scrapy.Item):
    title = scrapy.Field()  # 岗位名称
    salary = scrapy.Field() #岗位薪酬
    dq = scrapy.Field() #岗位地区
    requires = scrapy.Field() #教育水平
    labels = scrapy.Field() #岗位标签
    compLabels= scrapy.Field() #公司标签
    #link = scrapy.Field() #详情页链接
    compName = scrapy.Field() #公司名称
    compRemarks = scrapy.Field() #公司备注
    pass
