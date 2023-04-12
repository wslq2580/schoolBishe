# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
import pymysql
import openpyxl
import wordcloud



class JobfindingDB(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
            print('连接成功！')
        except:
            print('数据库连接失败')

        self.cursor = self.conn.cursor() #建立游标
        self.cursor.execute('create database if not exists liepin;') #建立数据库

        # 使用数据库
        self.cursor.execute('use liepin;')
        # 创建表格

        self.cursor.execute("create table if not exists liePinJob("
                            "title varchar(100) not null comment'岗位名称',"
                            "province varchar(10) not null comment'岗位所在省',"
                            "city varchar(30) not null comment'岗位所在市',"
                            "requireEduLevel varchar(100) not null comment'教育水平',"
                            "requireWorkYears varchar(100) not null comment'工作年数要求',"
                            "salary_lower varchar(100) not null comment'最低薪资',"
                            "salary_high varchar(100) not null comment'最高薪资',"
                            "labels varchar(100) not null comment'岗位标签',"
                            "recruiterName varchar(100) not null comment'招聘人姓名',"
                            "recruiterTitle varchar(100) not null comment'招聘人等级',"
                            "link varchar(400) PRIMARY KEY,compName varchar(120) not null comment'公司名称')")

        self.data =[]

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


    def _write_to_db(self):
        self.cursor.execute('truncate table liepinjob')
        self.cursor.executemany(
            'insert ignore into liePinJob (title,province,city,requireEduLevel,requireWorkYears,salary_lower,salary_high,labels,recruiterName,recruiterTitle,link,compName) '
            'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
            self.data
        )
        self.conn.commit()


    #添加数据
    def process_item(self, item, spider):
        title = item.get('title', '')
        salary = item.get('salary', '')
        if ('面' in salary):
            salary_lower = '薪资面议'
            salary_high = '薪资面议'
        elif ('k' in salary):
            salary_lower = str(salary.split("k")[0].split("-")[0]+'000')
            salary_high = str(salary.split("k")[0].split("-")[1]+'000')
        else:
            salary_lower = str(salary.split("k")[0].split("-")[0])
            salary_high = str(salary.split("k")[0].split("-")[1])

        dq = item.get('dq', '')
        if ('-' in dq):
            province = str(dq.split("-")[0])
            city = str(dq.split("-")[1])
        else:
            province = str(dq.split("-")[0])
            city = ''
        # if ('-' in dq):
        #     if('北京' or '上海' or '重庆' or '天津' in dq):
        #         province = str(dq.split("-")[0]+'市')
        #         city = str(dq.split("-")[1])
        #     elif('西藏'or'香港'or'澳门' in dq):
        #         province = str(dq.split("-")[0])
        #         city = str(dq.split("-")[1])
        #     elif('深圳' in dq):
        #         province = '广东省'
        #         city = '深圳市'
        #     elif ('武汉' in dq):
        #         province = '湖北省'
        #         city = '武汉市'
        #     elif ('杭州' in dq):
        #         province = '广东省'
        #         city = '深圳市'
        #     elif ('南京' in dq):
        #         province = '江苏省'
        #         city = '南京市'
        #     else:
        #         province = str(dq.split("-")[0] + '省')
        #         city = str(dq.split("-")[1])
        # else:
        #     if ('北京' or '上海' or '重庆' or '天津' in dq):
        #         province = str(dq.split("-")[0] + '市')
        #         city = str(dq.split("-")[1])
        #     elif ('西藏' or '香港' or '澳门' in dq):
        #         province = str(dq.split("-")[0])
        #         city = str(dq.split("-")[1])
        #     elif ('深圳' in dq):
        #         province = '广东省'
        #         city = '深圳市'
        #     elif ('武汉' in dq):
        #         province = '湖北省'
        #         city = '武汉市'
        #     elif ('杭州' in dq):
        #         province = '浙江省'
        #         city = '杭州市'
        #     elif ('南京' in dq):
        #         province = '江苏省'
        #         city = '南京市'
        #     else:
        #         province = str(dq.split("-")[0] + '省')
        #         city = str(dq.split("-")[1])
        requireEduLevel = item.get('requireEduLevel', '')
        requireWorkYears = item.get('requireWorkYears', '')
        labels = item.get('labels', '')
        recruiterName = item.get('recruiterName', '')
        recruiterTitle = item.get('recruiterTitle', '')
        link = item.get('link', '')
        compName = item.get('compName', '')

        self.data.append((title,province,city,requireEduLevel,requireWorkYears,salary_lower,salary_high,labels,recruiterName,recruiterTitle,link,compName))

        self._write_to_db()
        return item

#excel写数据
class JobfindingExcel(object):
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = 'liePinJob'
        self.ws.append(('title','dq','requireEduLevel','requireWorkYears','salary','labels','recruiterName','recruiterTitle','link','compName'))

    def close_spider(self, spider): #钩子方法，自动调用

        self.wb.save('猎聘网数据.xlsx') #爬虫关闭时自动保存excel

    def process_item(self, item, spider): #钩子方法，自动调用
        title = item.get('title','')
        dq = item.get('dq','')
        salary = item.get('salary', '')

        requireEduLevel = item.get('requireEduLevel', '')
        requireWorkYears = item.get('requireWorkYears', '')
        labels = item.get('labels', '')
        recruiterName = item.get('recruiterName', '')
        recruiterTitle = item.get('recruiterTitle', '')
        link = item.get('link','')
        compName = item.get('compName', '')
        self.ws.append((title,dq,requireEduLevel,requireWorkYears,salary,labels,recruiterName,recruiterTitle,link,compName))

        #把标签写入txt文本
        self.fp = open('liepinlabels.txt', 'a', encoding='utf-8')
        self.fp.write(labels)

        return item

#可视化

class JobfindingVision(object):
    def process_item(self, item, spider):
        pass
    def __init__(self):
        #os.remove('labels.txt')
        pass

    def close_spider(self, spider):
        pass


        #text = open('labels.txt', encoding='utf-8').read()
        #text = jieba.lcut(text)
        with open('liepinlabels.txt', 'r', encoding='utf-8') as fp:
            text = fp.read()
        #text = jieba.lcut(text)
        #text = " ".join(text)
        print('处理即将完成...')
        font_path = r'C:\Users\ThinkPad\PycharmProjects\schoolBishe\venv\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\SimHei.ttf'
        #words_pic = r'C:\Users\ThinkPad\PycharmProjects\schoolBishe\jobFinding\jobFinding\words_pic.png'
        wc=wordcloud.WordCloud(
            font_path=font_path,  # 显示中文，可以更换字体
            background_color='white',  # 背景色
            width=900,
            height=500,
            max_words=500,  # 最大显示单词数
            max_font_size=80,# 频率最大单词字体大小
            min_font_size=20
            #mask=matplotlib.image.imread(words_pic)
            #collections = False
        )
        # 传入需画词云图的文本
        wc.generate(text)
        image = wc.to_image()
        wc.to_file('猎聘网词云图.png')
        image.show()



