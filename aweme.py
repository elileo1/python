#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from pkcs7 import PKCS7Encoder
import time
import json
import base64
import requests
import threading

import multiprocessing
def hengda_get_smsCode():
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
        'Referer': 'https://hft02.evergrande.com/wechatPage/shareRegister.html?id=8e719a1f34904b50b2b514efab67fcb5&from=Android',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin':'https://hft02.evergrande.com',
        'Accept-Language': 'zh-cn',
        'Accept': '*/*',
        'Cookie' : "SERVERID=b193ee1e95a5363fdfc158babfe0d7c0|1517399135|1517399087; "
                   "gdxidpyhxdE=wUNU%2FSTUrV3tiWE4VrPoVH0lq2KYMldvyB5cIY%2FQ%2Bl%5CLG4KDfM8ScNog%2F%2FrVf7ZwRz7O0iUX9qm8paBsxaheii%2FTzS2CBiiDIujDemUCDdL6sWxfugJ4XWhuGsGph7qID7Q%2BMp%5CUWA3Lwx9GWuNLp1KGOU4P7PAHXgA63JXGTC4txfRJ%3A1517400050848; "
                   "_9755xjdesxxd_=32"
    }
    base_req = {
        "dateTime":"1517399157633",
        "type":"0",
        "phoneNumber":"18142877992",
        "sessionId":"E0CABF60-AFA8-4B58-B1B8-FF6FB8A69E3A",
        "NECaptchaValidate":"SG9O5AceTTm2zomyVoueymJF-7TOTfZ0ppiD.NZ7Xg6f-xmO89qClP8RNVDYcWfmy8vvo.ZVIbW.5Gor9DT1m5I7s_FUZfHIVMZRTLm5URcT5Yjo2PekEmmhVtPZg.vePD2JdrWGgm2oQ-zej0stZS9C1m7rZUSIIF.wY2PlVmsMXHSzx6p.mYwB8JIzEtbufU5Y_U7tCAcLha8Z.zaU4SOfpHaVpZZpARfhvG-oD0MamVKQQrBivRzvQXHbz6HhtdDRH4K9srL1aIkJO.TYsjwStvTiV__HtvhTCzO77tpzopWeivoQPQjfcUqFtA2GwiJoWHw4tJFCMMza.AT1Z9mm6nutrUHyss_AJ7J0A7KRovrDPNfZ.5RuxHrsAVxhC-WQSMTsa2lkD9sdmkEwT0sJfR9LMtMow_vyXm-.7BKQ0fEKa69NbHO280eYEeCsd2slzzuZRl6n7Dv7_T0sjJ6ySGjhxVwIzcxKb9JzeuJmhYdIETio7ttdDbA3",
        "captchaId":"df5690b5a45e4c00afb62305cee5fcf1"}
    result = requests.post(
        'https://hft02.evergrande.com/broker/rest/sms/getSmsCode',
        data=base_req, headers=headers)
    print result.json();





def updateData(itemId):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN',
        'Referer': 'http://aweme.snssdk.com',
        'Content-Type': 'application/json',
        'Accept-Language': 'zh-cn',
        'Accept': '*/*',
        'Cookie': "install_id=22997104463;login_flag=66b91938acd0eb6a487870b2c90bf80c;" +
                  "qh[360]=1;sessionid=05f95b6d15b93c2ca4df5ea9b7c2a4c5;" +
                  "sid_guard=05f95b6d15b93c2ca4df5ea9b7c2a4c5%7C1515500125%7C15552000%7CSun%2C%2008-Jul-2018%2012%3A15%3A25%20GMT;" +
                  "sid_tt=05f95b6d15b93c2ca4df5ea9b7c2a4c5;" +
                  "ttreq=1$1b0574d7ae2e02ee47f4f0db43bfe1e2d4144929;" +
                  "uid_tt=9d5cb1ebfa65c9a8ba7416a002dbec75"
    }
    base_req = {
        'item_id':itemId,
        'tab_type':"3",
        'play_delta':"1",
        'aweme_type':"0",
        'retry_type':"no_retry",
        'os_api':"22",
        'device_type':"OPPO%20R9m",
        'device_platform':"android",
        'ssmix':"a",
        'iid':"22997104463",
        'manifest_version_code':"169",
        'dpi':"480",
        'uuid':"863466039294292",
        'version_code':"169",
        'app_name':"aweme",
        'version_name':"1.6.9",
        'openudid':"6cbb4f55f20701f5",
        'device_id':"36488622464",
        'resolution':"1080*1920",
        'os_version':"5.1",
        'language':"zh",
        'device_brand':"OPPO",
        'ac':"wifi",
        'update_version_code':"1692",
        'aid':"1128",
        'channel':"oppo",
        '_rticket':"1515566742402",
        'retry_type':"retry_http",
        'os_api':"22",
        'device_type':"OPPO%20R9m",
        'device_platform':"android",
        'ssmix':"a",
        'iid':"22997104463",
        'manifest_version_code':"169",
        'dpi':"480",
        'uuid':"863466039294292",
        'version_code':"169",
        'app_name':"aweme",
        'version_name':"1.6.9",
        'openudid':"6cbb4f55f20701f5",
        'device_id':"36488622464",
        'resolution':"1080*1920",
        'os_version':"5.1",
        'language':"zh",
        'device_brand':"OPPO",
        'ac':"wifi",
        'update_version_code':"1692",
        'aid':"1128",
        'channel':"oppo",
        '_rticket':"1515566742462"
    }
    result = requests.post('http://aweme.snssdk.com/aweme/v1/aweme/stats/?os_api=22&device_type=OPPO+R9m&device_platform=android&ssmix=a&iid=22997104463&manifest_version_code=169&dpi=480&uuid=863466039294292&version_code=169&app_name=aweme&version_name=1.6.9&openudid=6cbb4f55f20701f5&device_id=36488622464&resolution=1080*1920&os_version=5.1&language=zh&device_brand=OPPO&ac=wifi&update_version_code=1692&aid=1128&channel=oppo&_rticket=1515566742462&ts=1515566737&as=a1853b2541f9ea36e5&cp=bc92ab5312595163e1', data=base_req)
    print result.json();

def testMultiThread():
    while True:
        for num in range(0, 250):
            threading.Thread(target=updateData("6509265084949204228"))


if __name__ == "__main__":
    hengda_get_smsCode();
    # for num in range(0, 10):
    #     p = multiprocessing.Process(target=testMultiThread)
    #     p.start()
