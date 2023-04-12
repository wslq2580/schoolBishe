import scrapy
import json
from ..items import JobfindingItem

class LiepinSpider(scrapy.Spider):
    name = "liePin"
    #allowed_domains = ["www.liepin.com"]
    #start_urls = ["http://www.liepin.c

    kw = input("猎聘爬虫已启动，请输入关键词：")
    page_num = int(input('您想爬取几页数据？（直接输入小写数字即可）'))
    def start_requests(self):
        global int
        true_url = 'https://apic.liepin.com/api/com.liepin.searchfront4c.pc-search-job'
        data = {
            "data": {
                "mainSearchPcConditionForm": {
                    "city": "410",
                    "compId": "",
                    "compKind": "",
                    "compName": "",
                    "compScale": "",
                    "compStage": "",
                    "compTag": "",
                    "currentPage": 0,
                    "dq": "410",
                    "eduLevel": "",
                    "industry": "",
                    "jobKind": "",
                    "key": self.kw,
                    "pageSize": 40,
                    "pubTime": "",
                    "salary": "",
                    "suggestTag": "",
                    "workYearCode": "0"
                },
                "passThroughForm": {
                    "ckId": "5sqka8lfa5dk8zbeqhzipiss7cwpeaha",
                    "scene": "hot_search",
                    "skid": "",
                    "fkid": "",
                    "suggest": None
                }
            }
        }
        #for page in range(self.page_num):
        for i in range(self.page_num):
            data["data"]["mainSearchPcConditionForm"]["currentPage"] = i
            print(data["data"]["mainSearchPcConditionForm"]["currentPage"])
            yield scrapy.Request(url=true_url, method='POST', body=json.dumps(data), callback=self.parse)

    def parse(self, response):
        str_json = json.loads(response.text)
        #str_json = json.loads(str_json)
        for data in str_json['data']['data']['jobCardList']:
            item = JobfindingItem()
            item['title'] = data['job']['title']
            item['dq'] = data['job']['dq']
            item['link'] = data['job']['link']
            item['requireEduLevel'] = data['job']['requireEduLevel']
            item['requireWorkYears'] = data['job']['requireWorkYears']
            item['salary'] = data['job']['salary']
            item['recruiterName'] = data['recruiter']['recruiterName']
            item['recruiterTitle'] = data['recruiter']['recruiterTitle']
            item['compName'] = data['comp']['compName']

            for label in data:
                item['labels'] = ','.join(data['job']['labels'])
            print(item['title'])
            yield item #数据提交给item管道处理
        return self.kw

