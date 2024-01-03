
'''
base64工具类
'''
import base64

# 加密
def encode(input):
    return base64.b64encode(input.encode('utf-8')).decode("gbk")

# 解密
def decode(input):
    return (base64.b64decode(input)).decode('gbk')
