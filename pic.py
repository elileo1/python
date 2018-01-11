#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib
import time
import Screenshot
import io
import webbrowser
import requests
import base64
from PIL import Image


api_key = 'ZpGGVxrMn6VMZUyDHLg7mxwz'
api_secret = '4vyGw9aVsxEee5xIM1AsuaP3KyvBltMG '
token = '24.894a366bafda51d8d0528bf810dd8a65.2592000.1518230663.282335-10672403'

if __name__ == "__main__":
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    Screenshot.check_screenshot()
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    im = Image.open("./answer.png")
    region = im.crop((0, 200, 1280, 300))
    imgByteArr = io.BytesIO()
    region.save(imgByteArr, format='PNG')
    image_data = imgByteArr.getvalue()
    base64_data = base64.b64encode(image_data)
    r = requests.post('https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
                      params={'access_token': token}, data={'image': base64_data})
    result = ''
    for i in r.json()['words_result']:
        result += i['words']
    print result
    # result = urllib.parse.quote(result)
    webbrowser.open('https://baidu.com/s?wd=' + result)
