# 获取拉钩网上，不同城市提供的python的职位信息
# 城市包括：北京、上海、深圳、广州、杭州、成都、南京、武汉、西安、厦门、长沙、苏州、天津 


import requests
import random
import time
import csv
import re

# 随机选取 user-agent
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 S'
    'afari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.307'
    '29; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.96'
    '3.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NE'
    'T CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Ver'
    'sion/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Vers'
    'ion/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 M'
    'obile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Versio'
    'n/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
    'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 S'
    'afari/534.13',
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobi'
    'le Safari/534.1+',
    'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.7'
    '0 Safari/534.6 TouchPad/1.0',
    'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) Appl'
    'eWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
    'UCWEB7.0.2.37/28/999',
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',

]

head = {
    'User-Agent': None,
    'Host': 'www.lagou.com',
    'Cookie': 'JSESSIONID=ABAAABAAAIAACBI4E49DCB3DBF49FE4D6C7C422B1162A'
              '1B; _ga=GA1.2.1144309098.1545206987; user_trace_token=20'
              '181219160949-74723a05-0365-11e9-9212-5254005c3644; LGSID=20'
              '181219160949-74723bf6-0365-11e9-9212-5254005c3644; PRE_UT'
              'M=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.ba'
              'idu.com%2Flink%3Furl%3DyzuE5y2UnNHqquyH2vFVdF8AKZblg5Y6V_2'
              'X87IMcBS%26wd%3D%26eqid%3De50ea420000e8ab4000000065c19f'
              'cc9; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=2018121'
              '9162905-25bb2077-0368-11e9-9212-5254005c3644; LGUID=20181'
              '219160949-74723e39-0365-11e9-9212-5254005c3644; Hm_lvt_423'
              '3e74dff0ae5bd0a3d81c6ccf756e6=1545206987; Hm_lpvt_4233e74'
              'dff0ae5bd0a3d81c6ccf756e6=1545208143; index_location_ci'
              'ty=%E5%85%A8%E5%9B%BD; _gid=GA1.2.1944889935.154520699'
              '1; TG-TRACK-CODE=search_code; SEARCH_ID=8d3253c7fcb44bb'
              'cbf96c0e60d3a5f00; isCloseNotice=0; X_HTTP_TOKEN=e715212'
              '6bb47efedb9417d9fd478e7e5; sensorsdata2015jssdkcross=%7'
              'B%22distinct_id%22%3A%22167c5855b4c1d8-0754c794a1918d-4c3'
              '12e7e-1327104-167c5855b4d479%22%2C%22%24device_id%22%3A%2'
              '2167c5855b4c1d8-0754c794a1918d-4c312e7e-1327104-167c5855b'
              '4d479%22%7D; sajssdk_2015_cross_new_user=1; LG_LOGIN_USE'
              'R_ID=8cac441bdb1507f2239e848648c0395e590387b12b68afa7138'
              'c64209355fa79; _putrc=75D59C81E2BB066E123F89F2B170EADC; l'
              'ogin=true; unick=qiuchunliu; showExpriedIndex=1; showExp'
              'riedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=9; g'
              'ate_login_token=763f28e8d1d2df2b18a726f84fbf03fafe96483c52b6f99e80699828103f4a50',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
}
# data 里的 pn 表示了爬取第几页
data = {
    'first': 'false',
    'pn': None,
    'kd': 'python'
}
for city in ['北京', '上海', '深圳', '广州', '杭州', '成都', '南京', '武汉', '西安', '厦门', '长沙', '苏州', '天津']:
    # for city in ['北京']:
    position_count = 0
    print('\n\n\n\n -------------------------------------------------------------此时在 {} 。。。。。\n\n\n'.format(city))
    try:
        url = 'https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false'.format(city)
        # 用这个 url 来获取html页面，找到该城市下 共有多少页的目标职位信息
        file = open('{}的职位.csv'.format(city), 'a+', newline='')
        writer = csv.writer(file, dialect='excel')
        writer.writerow(('职位', '工资', '经验', '学历', '公司规模'))  # 写入表头
        total_page_num = None
        head['User-Agent'] = random.choice(user_agent_list)
        resp_temp = requests.get('https://www.lagou.com/jobs/list_python?px=default&city={}'.format(city),
                                 headers=head
                                 )  # 获取 html
        resp_temp.encoding = 'utf-8'
        # print(resp_temp.status_code, '\n', resp_temp.text)
        get_total_page_num = int(re.findall(r'class="span totalNum">(.*?)</span>', resp_temp.text)[0])
        print('\n{} 中共有 {} 页\n'.format(city, get_total_page_num))
        # 通过解析得到共有多少索引页，总页数用于下边的 for 循环

        for pn in range(1, get_total_page_num+1):
            wait_count = 0  # 如果被反爬，则尝试几次，  如果还是失败，则跳过
            head['User-Agent'] = random.choice(user_agent_list)
            data['pn'] = pn
            print('正在获取第 %d 页' % pn)
            response = requests.post(url, headers=head, data=data)  # , proxies=proxies
            while '请稍后再访问' in response.text:
                # while 循环用于被反爬后再次的尝试
                wait_count += 1
                if wait_count == 10:
                    break  # break 表示再次尝试 10 次后就不再尝试了
                print('爬取被拦截，正在等待5s，然后重新爬取。。。')
                time.sleep(5)  # 再次尝试时，停留5s
                head['User-Agent'] = random.choice(user_agent_list)
                response = requests.post(url, headers=head, data=data)
            # print(head['User-Agent'])
            # print(response.status_code)
            response_json = response.json()  # 把获取到的字符串转为字典
            results = response_json['content']['positionResult']['result']
            # results 里是字典的集合，每一项字典包含了职位信息
            for result in results:
                item = {
                    "positionName": result["positionName"],
                    "workYear": result["workYear"],
                    "education": result["education"],
                    "companySize": result["companySize"],
                    "salary": result['salary']
                }
                # print(item)
                # 将信息写入 csv 文件
                writer.writerow((item['positionName'],
                                 item["salary"],
                                 item["workYear"],
                                 item["education"],
                                 item["companySize"]
                                 )
                                )
                position_count += 1  # 获取到的职位信息计数
                print('写入成功 %d 条职位信息' % position_count)
            # print(response_json['content']['positionResult']['result'])
            print('*********************************************************')
            time.sleep(2)
    except:
        print('\n出现错误，已跳过 --------------------------------------------\n')

