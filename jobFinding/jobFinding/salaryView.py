import pymysql
from pyecharts.charts import Pie
from pyecharts.charts import Bar
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.globals import ThemeType

try:
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
    print('连接成功！')
except:
    print('数据库连接失败')

cursor = conn.cursor()  # 建立游标
cursor.execute('use liepin;')
sql = "select requireWorkYears,CEILING (avg(cast(salary_lower as SIGNED)+cast(salary_high as SIGNED))) from liepinjob group by requireWorkYears;"
cursor.execute(sql)
data = cursor.fetchall()
dq = []
dq.extend(data)
print(dq)
pie = (
    Pie()
    .add("薪酬统计图", dq,rosetype='area')
    .set_global_opts(title_opts=opts.TitleOpts(title="饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
pie.render("薪酬统计图.html")

sql1 = "select requireWorkYears,CEILING(avg(salary_lower)),CEILING(avg(salary_high)) from liepinjob group by requireWorkYears;"
cursor.execute(sql1)
data1 = cursor.fetchall()
dq1 = []
dq1.extend(data1)
year = list(zip(*dq1))[0]
lowSalary = list(zip(*dq1))[1]
highSalary = list(zip(*dq1))[2]
print(year,lowSalary,highSalary)
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(year)
    .add_yaxis("最低薪资平均值",lowSalary)
    .add_yaxis("最高薪资平均值",highSalary)
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    .set_series_opts(markline_opts=["average"])
)

bar.render("薪酬条形图.html")