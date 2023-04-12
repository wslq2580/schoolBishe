import pymysql
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from pyecharts import options as opts
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
c = (
    Pie()
    .add("薪酬统计图", dq)
    .set_global_opts(title_opts=opts.TitleOpts(title="饼图"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)
c.render("薪酬统计图.html")
