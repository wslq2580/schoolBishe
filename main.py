import requests
import base64

url = 'https://bj.58.com/job/'
kw = input('输入关键字')
param = {
    'key':kw
}
headers = {
    'UserAgent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
resource = requests.get(url=url,params=param,headers=headers)#动态拼接参数
page_text = resource.text
fileName = kw+'.html'
with open(fileName,'w',encoding='utf-8')as fp:
    fp.write(page_text)
print('finish')