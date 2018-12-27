
import csv
import re
from pyecharts import Bar


city_list = ['北京', '上海', '深圳', '广州', '杭州', '成都', '南京', '武汉', '西安', '厦门', '长沙', '苏州', '天津']
result_dict = dict()

for city in city_list:
    openfile = open('{}的职位.csv'.format(city), 'r')
    get = csv.reader(openfile)

    count = 0
    sum_temp = 0
    for i in get:
        count += 1
        salary = i[1]
        salary_list = list(map(lambda x: int(re.findall(r'\d{,3}', x)[0]), salary.split('-')))
        sum_temp += sum(salary_list)/2

    salary_avg = sum_temp/count
    result_dict[city] = salary_avg
print('计算完成')

for i in result_dict:
    print(i, '%3.2f' % result_dict[i])


dict_sort = sorted(result_dict, reverse=True)

city_salary = [result_dict[money] for money in city_list]
# 横纵坐标
chart = Bar("图表")
# 图表标题
chart.add('', city_list, city_salary)
# 生成图表
chart.render('somename.html')
# 将图标写入网页中，进行可视化，因为pycharm里好像无法显示
print('图标生成')
