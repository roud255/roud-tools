import base64
import hashlib
import re
import sys


'''
加密常用
'''

def s_md5(text,s,e):
    try:
        if(s==0 and e==0):
            res = str(hashlib.md5((text).encode("utf-8")).hexdigest())
        else:
            res = str(hashlib.md5((text).encode("utf-8")).hexdigest()[s:e])
        return res
    except Exception as e:
        res = 'An error occurred,please see the function---'+str(sys._getframe().f_code.co_name)+'---the e.args:'+str(e.args)
        return res

def s_base64(text):
    try:
        res1 = str(base64.b64encode((text).encode('utf-8')))
        res = str(re.findall('b\'(.+?)\'', res1)[0])
        return res
    except Exception as e:
        res = 'An error occurred,please see the function---'+str(sys._getframe().f_code.co_name)+'---the e.args:'+str(e.args)
        return res