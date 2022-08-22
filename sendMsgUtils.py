import json
import requests
import logging


enableLog = False  # 是否开启日志

# 发生信息 （公众号即使达推送）,需要更改的话，改这里，注意 参数和名称不能改，改逻辑就好
def send_msg(head, body, key):
    try:

        if enableLog:
            logging.info('----------start send_msg')
        url = 'http://push.ijingniu.cn/send'
        data = {
            'key': key,
            'head': head,
            'body': body
        }
        requests_post = requests.post(url=url, data=data)
        if enableLog:
            logging.info(requests_post.text)
            logging.info(requests_post.text)
        if requests_post.ok:
            return json.loads(requests_post.text)
        else:
            return {
                'code': '402',
                'msg': '发送通知失败'
            }
    except Exception as N:
        print("发送失败")
        if enableLog:
            logging.error("发送失败" + N)
            logging.error('发送推送信息失败')


LogName = 'sendMsgLog.txt'
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                    filename=LogName,
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    # 日志格式
                    )
