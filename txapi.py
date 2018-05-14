import requests
import md5sign

def get_content(plus_item):
    # url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"  # 情感分析的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"  # 聊天的API地址
    plus_item = plus_item.encode('utf-8')
    payload = md5sign.get_params(plus_item)#获取请求参数
    r = requests.get(url,params=payload)
    r = r.json()
    return r["data"]["answer"]

if __name__ == '__main__':
    while True:
        comment = input('我：')
        if comment == 'q':
            break
        answer=get_content(comment)
        print('机器人：，'+answer)
