import requests,urllib3,json
from typing import Literal as rangeList
class Email:
    def __init__(
            self,
            To:str,
            text:str | int,
            Title:str,
            Token:str,#توکن دسترسی
            Input: rangeList['info','app','Login','support'] = 'info',
        ) -> None:
        self.To=To
        self.text=text
        self.Title=Title
        self.Input=Input
        self.Token=Token
    def Send(self):
        Data={
            'email':self.To,
            'text':self.text,
            'head':self.Title,
            'token':self.Token,
            'title':self.Input
        }
        http = urllib3.PoolManager()
        url = 'https://api-free.ir/api2/email.php'
        response = http.request(
            'POST',
            url,
            fields=Data
        )
        pars=json.loads(response.data.decode('utf-8'))
        print(pars)
        if pars['ok']:return {
            'state':'ok',
            'code':200
        }
        else:return False
