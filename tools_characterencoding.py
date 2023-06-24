'''
用于爬虫请求中的响应编码格式转换
'''
def show_utf8(response):
    return response.content.decode('utf-8')
def show_escape(response):
    return response.content.decode('unicode_escape')
def show_gbk(response):
    return response.content.decode('gbk')