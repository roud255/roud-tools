import base64
import os

import ddddocr
import requests
from tools_const import get_headers_only_user_agent
from tools_file import mkdirs

'''
验证码识别带带弟弟版，将验证码下载保存到本地后识别
'''

headers = get_headers_only_user_agent()
'''
验证码图片本地保存路径
'''
captcha_path = ""

ocr = ddddocr.DdddOcr(old=True)
mkdirs(captcha_path)

'''
方法1
传入：验证码图片链接、http代理
返回：验证码识别结果、cookies
'''
def ocr(code_url, proxies):
    img_result = requests.get(url = code_url, headers= headers, timeout=3, proxies=proxies)
    img_data = img_result.content
    img_cookies = img_result.cookies
    with open(captcha_path, 'wb') as f:
        f.write(img_data)
    with open(captcha_path, 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    os.remove(captcha_path)
    arr = []
    arr.append(res)
    arr.append(img_cookies)
    return arr

'''
方法2
传入：验证码图片链接、cookies、http代理
返回：验证码识别结果、cookies
'''
def ocr2(url,cookies, proxies):
    img_result = requests.get(url = url, headers= headers, cookies=cookies, timeout=3, proxies=proxies)
    img_data = img_result.content
    img_cookies = img_result.cookies
    with open(captcha_path, 'wb') as f:
        f.write(img_data)
    with open(captcha_path, 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    os.remove(captcha_path)
    arr = []
    arr.append(res)
    arr.append(img_cookies)
    return arr

'''
方法3
传入：图片的base64编码、用户标识flag
返回：验证码识别结果、用户标识flag
'''
def ocr_base64(img_data_base64, flag):
    with open(captcha_path, 'wb') as f:
        f.write(base64.b64decode(img_data_base64))
        f.close()
    with open(captcha_path, 'rb') as f:
        image = f.read()
    res = ocr.classification(image)
    os.remove(captcha_path)
    arr = []
    arr.append(res)
    arr.append(flag)
    return arr