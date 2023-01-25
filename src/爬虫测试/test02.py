from bs4 import BeautifulSoup
import requests

from xpinyin import Pinyin
# 设置请求方式和请求头
session = requests.Session()
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
       (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41'
}

# 实例拼音转换对象
p = Pinyin()
city = '武汉'
citycode = p.get_pinyin(city, '')

# 测试是否存在该城市的数据
url = 'https://tianqi.2345.com/' + citycode + '2d/57494.htm'

# 获取网页并转为BeautifulSoup对象
req = session.get(url, headers=headers)
soup = BeautifulSoup(req.text, 'html.parser')
results = soup.select(
    '#today-main-deatil > div.weather-mess.pd-t0 > div.hours-info > div.real-mess > div.real-icon.wea-white-icon > span')
wendu = list(results)[0].getText()
print(wendu)