"""https://geoapi.qweather.com/v2/city/lookup?location=%E6%B4%AA%E6%B9%96&key
=401eb7a6b3fa458d89a4bd13433c4a96 """
import json
import requests
import sys

city = '武汉'
# cityid = '101200101'
keyId = '401eb7a6b3fa458d89a4bd13433c4a96'
url_city = 'https://geoapi.qweather.com/v2/city/lookup?location=%s&key=%s' % (city, keyId)

response = requests.get(url_city)
cityData = json.loads(response.text)


# 定义确认输入城市的函数
def indentify(data):
    # 判断输入是否正确
    if data['code'] == '200':
        return True
    else:
        return False


# 获取城市id
def get_cityid(data, cityname):
    c = data['location']
    for i in c:
        if i['name'] == cityname:
            return cityname, i['id']
        else:
            return (c[0])['name'], (c[0])['id']


if indentify(cityData):
    pass
else:
    print('无该城市信息，请重试')
    sys.exit()

city, cityId = get_cityid(cityData, city)
url_weather = 'https://devapi.qweather.com/v7/weather/now?location=%s&key=%s' % (cityId, keyId)
response = requests.get(url_weather)
weatherData = json.loads(response.text)
w = weatherData['now']
response_txt = '当前%s的天气为%s\n气温%s°c 体感温度%s°c\n%s%s级 风速%s公里/小时\n更新时间%s' \
               % (city, w['text'], w['temp'], w['feelsLike'], w['windDir'], w['windScale'], w['windSpeed'], w['obsTime'][0:16])
print(response_txt)
