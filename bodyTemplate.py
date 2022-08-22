"""
    天气数据:
        "city": "广州",
        "lastUpdateTime": "2022-08-22 11:55:08",
        "date": "2022-08-22",
        "weather": "阴",
        "temp": 38.0,
        "humidity": "70%",
        "wind": "南风2级",
        "pm25": 20.0,
        "pm10": 26.0,
        "low": 26.0,
        "high": 38.0,
        "airData": "26",
        "airQuality": "优",
        "dateLong": 1661097600000,
        "weatherType": 2,
        "windLevel": 2,
        "province": "广东"

    body['love_days']数据：
        'days': 920,  #天
        'hours': 23,  #小时
        'minute': 25, #分钟
        'seconds': 59 #秒



        注意:自己写模板时，类似body['weather']['weather'] 得到的值是数字，不能直接和文字拼接
        需要放数字转为文字，再拼接


        总结 需要用str( body['weather']['weather'] )  -> 得到是文字
"""


def templateByBody(body):
    return {
        '今日天气': body['weather']['weather'],
        '当前温度': body['weather']['temp'],
        '高低温': str(body['weather']['low'])+'~'+ str(body['weather']['high']),
        # '最低温度': body['weather']['low'],
        # '最高温度': body['weather']['high'],
        '湿度': body['weather']['humidity'],
        '风力': body['weather']['wind'],
        'pm25': body['weather']['pm25'],
        'I have been in love with you for':
            str(body['love_days']['days']) + "天" +
            str(body['love_days']['hours']) + "时" +
            str(body['love_days']['minute']) + "分" +
            str(body['love_days']['seconds']) + "秒",
        '距离你生日还有': str(body['birthday_left']) + '天',
        '每日一句': body['words']
    }
