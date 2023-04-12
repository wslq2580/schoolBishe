import pymysql
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType, GeoType

try:
    conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
    print('连接成功！')
except:
    print('数据库连接失败')

cursor = conn.cursor()  # 建立游标
cursor.execute('use liepin;')
sql = "select province,count(title) from liepinjob group by province;"
cursor.execute(sql)
data = cursor.fetchall()
dq = []
dq.extend(data)
# new_t = [(*t[:1], *map(int, t[1:2])) for t in dq]
titlename = '岗位所在地统计'

print(dq)

geo = (Geo(init_opts=opts.InitOpts(width='1200px',
                                   height='600px',
                                   theme='romantic',
                                   is_fill_bg_color=True),
           is_ignore_nonexistent_coord=True)
    .add_schema(maptype='china',
                label_opts=opts.LabelOpts(is_show=True))  # 显示label  省名
    .add('岗位数量',
         data_pair=dq,
         symbol_size=8,
         # geo_cities_coords=geo_cities_coords
         )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
    title_opts=opts.TitleOpts(title='星巴克门店在中国的分布'),
    visualmap_opts=opts.VisualMapOpts(max_=100,is_piecewise=True,split_number = 10)
    )
)

geo.render("岗位所在地统计.html")