# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 12:55:04 2021

@author: jmaeda
"""

import requests

class WeatherResponder:
    """WeatherResponderクラス
       Weather Hacksに接続して、ユーザーが希望する地域の天気予報を取得する
    """
    def get_weather(self, place, id):
        """Weath Hacksに接続して天気予報を取得する
        
        Parameters:
            place(str) : ユーザーが希望する地域名
            id(str) : 地域id
            
        returns:
            str : 今日、明日、明後日の天気予報を伝える応答フレーズ
        """
        # weather　HacksのURL
        # url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
        # livedoorの天気予報のURLは廃止されたので代替のURLを検索して以下URLにした
        url = 'https://weather.tsukumijima.net/api/forecast'
        # 'city'をキー、idをその値とした辞書オブジェクトを作成
        payload = {'city': id}
        # 天気予報を取得する
        weather_data = requests.get(url, params=payload).json()
        forecast = '～' + place + 'の天気予報～\n'
        # 今日、明日、明後日の天気を順番に取り出して応答を作る
        for weather in weather_data['forecasts']:
            forecast += (
                '\n'
                + weather['dateLabel'] 
                + 'の天気は'
                + weather['telop']
            )
            text1 = weather['image'] 
            imgurl = text1['url']
        #    img1 = requests.get(imgurl)
        return forecast