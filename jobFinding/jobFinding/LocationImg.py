from itertools import chain
import pandas as pd

import pymysql
from pyecharts.charts import Map, Geo  # 注意这里与老版本pyecharts调用的区别
from pyecharts import options as opts



class LocationImg(object):
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
        print('连接成功！')
    except:
        print('数据库连接失败')

    cursor = conn.cursor() #建立游标
    cursor.execute('use liepin;')
    sql = "select province,count(title) from liepinjob group by province;"
    cursor.execute(sql)
    # words=[]
    # data=words.extend(cursor.fetchall())  # 获取所有数据
    data = cursor.fetchall()
    dq = []
    dq.extend(data)
    #new_t = [(*t[:1], *map(int, t[1:2])) for t in dq]
    print(dq)
    titlename = '岗位所在地统计'
    # china_city = (
    #     Map()
    #     .add(
    #         series_name='岗位所在地统计',
    #         data_pair=values,
    #         maptype="china",
    #         is_map_symbol_show=True,                    #此处控制在地图上是否显示红点，data_city中有的市名才会在地图中显示红点呦
    #         label_opts=opts.LabelOpts(is_show=True),#此处控制在地图上是否显示名称
    #     )
    #     .set_global_opts(
    #         title_opts=opts.TitleOpts(title=titlename),
    #         visualmap_opts=opts.VisualMapOpts(
    #             is_show=True,
    #             type_= 'color',
    #             min_=0,
    #             max_=50,
    #             is_piecewise=True,
    #             split_number = 10
    #                  #定义左下角图例为分段型，默认为连续的图例
    #         ),
    #     )
    #     .render(titlename+".html")

    def map_visualmap(dq) -> Map:
        c = (
            Map(opts.InitOpts(width='1200px', height='600px'))  # opts.InitOpts() 设置初始参数:width=画布宽,height=画布高
                .add(series_name='岗位所在地统计', data_pair=dq, maptype="china")  # 系列名称(显示在中间的名称 )、数据 、地图类型
                .set_global_opts(
                title_opts=opts.TitleOpts(title="地图"),
                visualmap_opts=opts.VisualMapOpts(max_=150, min_=0,is_piecewise=True),
            )
        )
        return c

    map = map_visualmap(dq)
    map.render(path='岗位所在地统计.html')

    # geo = Geo(
    #     "全国部分城市空气质量",
    #     title_color="#fff",
    #     title_pos="center",
    #     width=800,
    #     height=600,
    #     background_color="#404a59",
    # )
    # attr, value = geo.cast(dq)
    # geo.add(
    #     "",
    #     attr,
    #     value,
    #     visual_range=[0, 200],
    #     visual_text_color="#fff",
    #     symbol_size=15,
    #     is_visualmap=True,





