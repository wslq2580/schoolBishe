from collections import Counter
from itertools import chain

from pyecharts.charts import Map3D
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import pymysql

##从txt读labels
# class WordCloud(object):
#     with open('liepinlabels.txt', 'r+', encoding='utf-8') as fp:
#         words = []
#         for line in fp.readlines():
#             #传入字符串，返回分词的列表
#             words.extend(line[:-1].split(','))
#         print(words)
#
#     #对words列表中的分词进行数量统计
#     words_dict = dict(Counter(words))
#
#     #词云图的数据类型为列表嵌套元组：[(word1, count1), (word2, count2)]
#     #将words_dict中的数据转换成需要的格式
#     data_pair = [(k,v) for k,v in words_dict.items()]
#     wordcloud = WordCloud()
#
#     wordcloud.add(
#         series_name = '词频分析',
#         data_pair = data_pair
#         # 词云图轮廓，有 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star' 可选
#         #shape = 'star',
#         # 自定义的图片（目前支持 jpg, jpeg, png, ico 的格式.
#         # 注：如果使用了 mask_image 之后第一次渲染会出现空白的情况，再刷新一次就可以了（Echarts 的问题）
#         #mask_image = '' ,
#     )
#     wordcloud.set_global_opts(title_opts = opts.TitleOpts(title = '词云图'))
#     wc = wordcloud
#     wc.render('labels.html')

##从数据库读labels

class WordCloud(object):
    try:
        conn = pymysql.connect(host='localhost', user='root', passwd='123456', port=3306)
        print('连接成功！')
    except:
        print('数据库连接失败')

    cursor = conn.cursor() #建立游标
    cursor.execute('use liepin;')
    column_list = "labels"
    table = "liepinjob"
    sql = "select " + column_list + " from " + table
    cursor.execute(sql)
    # words=[]
    # data=words.extend(cursor.fetchall())  # 获取所有数据
    data = cursor.fetchall()
    resultlist = list(chain.from_iterable(data))
    words = []
    for line in resultlist:
        #传入字符串，返回分词的列表
        words.extend(line[:-1].split(','))
    print(words)
    #对words列表中的分词进行数量统计
    words_dict = dict(Counter(words))

    #词云图的数据类型为列表嵌套元组：[(word1, count1), (word2, count2)]
    #将words_dict中的数据转换成需要的格式
    data_pair = [(k,v) for k,v in words_dict.items()]
    wordcloud = WordCloud()

    wordcloud.add(
        series_name = '词频分析',
        data_pair = data_pair
        # 词云图轮廓，有 'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star' 可选
        #shape = 'star',
        # 自定义的图片（目前支持 jpg, jpeg, png, ico 的格式.
        # 注：如果使用了 mask_image 之后第一次渲染会出现空白的情况，再刷新一次就可以了（Echarts 的问题）
        #mask_image = '' ,
    )
    wordcloud.set_global_opts(title_opts = opts.TitleOpts(title = '词云图'))
    wc = wordcloud
    wc.render('labels.html')
    cursor.close()
    conn.close()

##3Dmap
# example_data = [
#     ("黑龙江", [127.9688, 45.368, 100]),
#     ("内蒙古", [110.3467, 41.4899, 400]),
#     ("吉林", [125.8154, 44.2584, 700]),
#     ("辽宁", [123.1238, 42.1216, 500]),
#     ("河北", [114.4995, 38.1006, 335]),
#     ("天津", [117.4219, 39.4189, 300]),
#     ("山西", [112.3352, 37.9413, 370]),
#     ("陕西", [109.1162, 34.2004, 670]),
#     ("甘肃", [103.5901, 36.3043, 570]),
#     ("宁夏", [106.3586, 38.1775, 300]),
#     ("青海", [101.4038, 36.8207, 300]),
#     ("新疆", [87.9236, 43.5883, 300]),
#     ("西藏", [91.11, 29.97, 300]),
#     ("四川", [103.9526, 30.7617, 300]),
#     ("重庆", [108.384366, 30.439702, 300]),
#     ("山东", [117.1582, 36.8701, 300]),
#     ("河南", [113.4668, 34.6234, 300]),
#     ("江苏", [118.8062, 31.9208, 300]),
#     ("安徽", [117.29, 32.0581, 300]),
#     ("湖北", [114.3896, 30.6628, 900]),
#     ("浙江", [119.5313, 29.8773, 300]),
#     ("福建", [119.4543, 25.9222, 308]),
#     ("江西", [116.0046, 28.6633, 300]),
#     ("湖南", [113.0823, 28.2568, 300]),
#     ("贵州", [106.6992, 26.7682, 900]),
#     ("广西", [108.479, 23.1152, 300]),
#     ("海南", [110.3893, 19.8516, 300]),
#     ("上海", [121.4648, 31.2891, 1300]),
# ]
#
# def set_map3d():
#     map3d = Map3D(init_opts=opts.InitOpts(width='1200px',height='700px'))
#     map3d.add(
#         series_name = '公司所在地区',
#         data_pair = example_data,
#         #叠加图的类型
#         type_ = ChartType.BAR3D,
#         maptype='china',
#         #控制柱状图的图元样式
#         itemstyle_opts=opts.ItemStyleOpts(
#             color = '#FF0033',
#             #设置柱子的透明度，支持从 0 到 1 的数字，为 0 时不绘制该图形
#             #opacity=1
#         ),
#         #设置柱子的标签
#         label_opts=opts.LabelOpts(
#             is_show=True,
#             #设置标签的内容(标签内容格式器),支持字符串模板和回调函数
#             # # 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）
#             #formatter='{b}{c}',字符串模板
#             #回调函数，需要先引入JsCode,from pyecharts.commons.utils import JsCode
#             #不论时字符串还是回调函数都支持\n,\t，但是需要用双斜杠表示
#             formatter=JsCode("function(data){return data.name +'\\n'+ data.value[2];}")
#         ),
#         #配置选中柱子的标签
#         emphasis_label_opts=opts.LabelOpts(
#             is_show=True
#         ),
#         #设置选中的柱子的图元样式
#         emphasis_itemstyle_opts=opts.ItemStyleOpts(
#             color='#33FF00'
#         )
#     )
#     #添加底层地图
#     map3d.add_schema(
#         maptype='china',
#         #底层地图的厚度
#         region_height=1,
#         is_show_ground=True,
#         itemstyle_opts=opts.ItemStyleOpts(
#             #底层地图的颜色
#             color = 'blue',
#             #图形的描边颜色，即地图中区域分界线的颜色
#             border_color='yellow',
#             #分界线的类型,'dashed', 'dotted'
#             border_type='dashed',
#             #分界线的宽度
#             border_width=1
#         ),
#         #设置底层地图的label,
#         emphasis_label_opts=opts.LabelOpts(
#             #设置选中高亮区域不显示标签
#             is_show=False
#         ),
#         #设置高亮区域的图元样式
#         emphasis_itemstyle_opts=opts.ItemStyleOpts(
#             #设置选中区域显示为绿色
#             color = 'green'
#         ),
#         shading='lambert',
#         #设置光照，显示阴影
#         light_opts=opts.Map3DLightOpts(
#             #主光源的颜色
#             main_color='#FFFFCC',
#             # 主光源是否投射阴影。默认为关闭。
#             # 开启阴影可以给场景带来更真实和有层次的光照效果。但是同时也会增加程序的运行开销。
#             is_main_shadow =  True
#         )
#     )
#     map3d.set_global_opts(
#         title_opts=opts.TitleOpts(title='三维地图叠加柱状图'),
#         #视觉映射配置项，设置颜色过渡
#         visualmap_opts=opts.VisualMapOpts(
#             is_show=True,
#             type_='color',
#             min_ = 100,
#             max_ = 1300,
#             range_color=['red','orange','yellow','green','blue','purple'],
#             is_piecewise=True
#         )
#     )
#     return map3d
#
# map3d = set_map3d()
# map3d.render('map3d.html')
