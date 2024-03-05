import requests,urllib3
from typing import Optional, Union, Literal
class Email:
    def __init__(
            self,
            To:str,
            text:str | int,
            Title:str,
            Input: Literal['info','app','Login','support'] = 'info',
        ) -> None:
        self.To=To
        self.text=text
        self.Title=Title
        self.Input=Input
    def Send(self):
        Data={
            'email':self.To,
            'text':self.text,
            'head':self.Title,
            'from':self.Input
            }
        http = urllib3.PoolManager()
        url = 'https://api-free.ir/api/email.php'
        response = http.request(
            'POST',
            url,
            fields=Data
        )
        if response.json()['ok']:return {
            'state':'ok',
            'code':200
        }
        else:return False