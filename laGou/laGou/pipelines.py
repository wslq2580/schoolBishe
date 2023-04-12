# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter
import os
#from spiders.liePin import LiepinSpider
import scrapy
from xlutils.copy import copy
import cursor as cursor
import xlrd,xlwt
from itemadapter import ItemAdapter
import pymysql
from wordcloud import WordCloud
import numpy as np
import PIL.Image as Image
import openpyxl
import wordcloud
import jieba

class laGouDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
            print('连接成功！')
        except:
            print('数据库连接失败')

        self.cursor = self.conn.cursor() #建立游标
        self.cursor.execute('create database if not exists lagou;') #建立数据库

        # 使用数据库

        self.cursor.execute('use lagou;')
        print('选中数据库')
        #

        self.cursor.execute("create table if not exists laGouJob(title varchar(100) not null comment'岗位名称',salary varchar(80) not null comment'岗位薪酬',dq varchar(100) not null comment'岗位地区',requires varchar(100) not null comment'岗位需求', labels varchar(100) not null comment'岗位标签', compName varchar(120) PRIMARY KEY,compRemarks varchar(200) not null comment'公司备注')")
        print('创建表格')
        self.data =[]

    def close_spider(self,spider):

        self.conn.close()


    def _write_to_db(self):
        print('表格中写入数据')
        self.cursor.executemany(
            'insert ignore into lagoujob (title,dq,salary,requires,labels,compName,compRemarks) values(%s,%s,%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()


    #添加数据
    def process_item(self, item, spider):
        title = item.get('title', '')
        salary = item.get('salary', '')
        dq = item.get('dq', '')
        requires = item.get('requires', '')
        labels = item.get('labels', '')
        compName = item.get('compName', '')
        compRemarks = item.get('compRemarks','')

        self.data.append((title,dq,salary,requires,str(labels),compName,compRemarks))

        self._write_to_db()

            # label = ''.join(item['labels'])
        return item

#excel写数据
class laGouExcel(object):
    def __init__(self):
        print("正在初始化表格")
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'lagouJob'
        self.ws.append(('title','dq','salary','requires','labels','compName','compRemarks'))

    def close_spider(self, spider): #钩子方法，自动调用
        print("正在保存表格")
        self.wb.save('拉勾网数据.xlsx') #爬虫关闭时自动保存excel

    def process_item(self, item, spider):
        title = item.get('title', '')
        salary = item.get('salary', '')
        dq = item.get('dq', '')
        requires = item.get('requires', '')
        labels = item.get('labels', '')
        compName = item.get('compName', '')
        compRemarks = item.get('compRemarks', '')
        self.ws.append((title,dq,salary,requires,str(labels),compName,compRemarks))
        print("正在添加数据至表格")
        return item

#可视化

class laGouVision(object):
    def process_item(self, item, spider):
        labels = item.get('labels', '')
        self.file.write(str(labels))
        with open('lagoulabels.txt', 'r', encoding='utf-8') as fp:
            text = fp.read()
        textr = jieba.lcut(text)
        # text = " ".join(text)
        print('处理即将完成...')
        font_path = r'C:\Users\ThinkPad\PycharmProjects\schoolBishe\venv\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\SimHei.ttf'
        # words_pic = r'C:\Users\ThinkPad\PycharmProjects\schoolBishe\jobFinding\jobFinding\words_pic.png'
        wc = wordcloud.WordCloud(
            font_path=font_path,  # 显示中文，可以更换字体
            background_color='white',  # 背景色
            width=900,
            height=500,
            max_words=400,  # 最大显示单词数
            max_font_size=80,  # 频率最大单词字体大小
            min_font_size=20
            # mask=matplotlib.image.imread(words_pic)
            # collections = False
        )
        # 传入需画词云图的文本
        wc.generate(text)
        image = wc.to_image()
        wc.to_file('拉勾网词云图.png')
        image.show()

    def __init__(self):
        #os.remove('labels.txt')
        pass

    def close_spider(self, spider):
        self.file.close()

    def open_spider(self, spider):
        self.file = open('lagoulabels.txt', 'w')


