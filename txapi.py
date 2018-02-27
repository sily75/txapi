import requests
import md5sign
import re

def get_content(plus_item):
    # url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textpolar"  # 情感分析的API地址
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"  # 聊天的API地址
    payload = md5sign.get_params(plus_item)#获取请求参数
    r = requests.get(url,params=payload)
    return r.json()["data"]["answer"]

if __name__ == '__main__':
    while True:
        comment = input('我：')
        if comment == 'q':
            break
        #不能有空白符，并且只能识别200字节。comment不转utf-8也可以。
        comment = re.sub(r'\s','',comment)
        # text,polar,confd=get_content(comment)
        answer=get_content(comment)
        # print('文本：'+text+'\n'+'情感倾向：'+str(polar)+'\n'+'程度：'+str(confd))
        print('机器人：，'+answer)
