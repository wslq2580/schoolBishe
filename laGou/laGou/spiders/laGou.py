import scrapy
from ..items import LagouItem
from urllib.parse import urlencode

class LagouPySpider(scrapy.Spider):
    name = "laGou"

    # allowed_domains = ["www.lagou.com"]

    kd = input("拉钩爬虫已启动，请输入关键词：")
    pn = int(input('您想爬取第几页数据？（直接输入小写数字即可）：'))

    def start_requests(self):
        start_urls = "https://www.lagou.com/wn/jobs?"
        for i in range(1, self.pn+1):
            params = {
                'kd': self.kd,
                'pn': i,
                'fromSearch': 'true'
                }
            base_urls = start_urls
            new_urls = base_urls+urlencode(params)
            yield scrapy.Request(url=new_urls,callback=self.parse)

    def parse(self, response):

        job_list = response.xpath("//div[@class='list__YibNq']/div")
        for job in job_list:
            item = LagouItem()
            item['title'] = job.xpath("./div[1]/div/div/a/text()")[0].get()
            item['dq'] = job.xpath("./div[1]/div/div/a/text()")[1].get()
            #item['link'] = job_list.xpath("")
            item['requires'] = job.xpath("./div[1]/div/div[2]/text()")[0].get()
            #item['requireWorkYears'] = job_list['job']['requireWorkYears']
            item['compLabels'] = ''.join(job.xpath("./div[1]/div/div[2]/text()")[1].get())
            item['compName'] = job.xpath("div/div[2]/div/a/text()")[0].get()
            item['compRemarks'] = job.xpath("./div[2]/div[2]/text()")[0].get()
            item['salary'] = job.xpath("./div[1]/div/div[2]/span/text()")[0].get()
            item['labels'] = job.xpath("./div[2]/div/span/text()").getall()
            yield item


