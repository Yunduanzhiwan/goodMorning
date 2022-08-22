import math
import requests

import bodyTemplate
import sendMsgUtils
from getParameter import *
from bodyTemplate import templateByBody


def getWeather(city='广州'):
    url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
    res = requests.get(url).json()
    weather = res['data']['list'][0]
    return weather


def getWords():  # 彩虹屁
    words = requests.get("https://api.shadiao.pro/chp")
    if words.status_code != 200:
        return getWords()
    return words.json()['data']['text']


def getLoveDays():  # 恋爱过去了多少天
    delta = today - datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")

    val = delta.seconds

    seconds = val % 60
    val = math.floor(val / 60)

    minute = val % 60
    val = math.floor(val / 60)

    hour = val

    res = {
        'days': delta.days,
        'hours': hour,
        'minute': minute,
        'seconds': seconds
    }

    return res


def getBirthday():
    next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
    if next < datetime.now():
        next = next.replace(year=next.year + 1)
    return (next - today).days

def getBody():
    weather = getWeather(city)
    love_days = getLoveDays()
    birthday_left = getBirthday()
    words = getWords()

    return {
        'weather': weather,
        'love_days': love_days,
        'birthday_left': birthday_left,
        'words': words
    }


if __name__ == '__main__':
    res = templateByBody(getBody())
    resBody = ''
    for item in res.keys():
        resBody += str(item) + ": "
        resBody += str(res[item]) + "\n"
    msg = sendMsgUtils.send_msg(resTitle, resBody, sendKey)
    print(msg)
