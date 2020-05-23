from django.conf import settings

import requests



class OpenId:
    """微信小程序获取OPENID"""
    def __init__(self, jscode):
        self.url = 'https://api.weixin.qq.com/sns/jscode2session'
        self.app_id = settings.APPID
        self.app_secret = settings.APPSECRET
        self.jscode = jscode

    def get_openid(self):
        url = self.url + "?appid=" + self.app_id + "&secret=" + self.app_secret + "&js_code=" + self.jscode + "&grant_type=authorization_code"
        res = requests.get(url)
        try:
            openid = res.json()['openid']
            session_key = res.json()['session_key']
        except KeyError:
            return 'fail'
        else:
            return openid, session_key

