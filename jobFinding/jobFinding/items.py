# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#猎聘item
class JobfindingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #岗位名称
    salary = scrapy.Field() #岗位薪酬
    salary_lower = scrapy.Field()
    salary_high = scrapy.Field()
    dq = scrapy.Field() #岗位地区
    province = scrapy.Field() #岗位所在省
    city = scrapy.Field() #岗位所在市
    requireEduLevel = scrapy.Field() #教育水平
    requireWorkYears = scrapy.Field() #工作年数要求
    labels = scrapy.Field() #岗位标签
    recruiterName = scrapy.Field() #招聘人姓名
    recruiterTitle = scrapy.Field() #招聘人等级
    link = scrapy.Field() #详情页链接
    compName = scrapy.Field() #公司名称
    pass