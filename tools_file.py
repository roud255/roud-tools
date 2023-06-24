import os
'''
文件工具类
'''

'''
传入一个文件路径，目录不存在则创建
'''
def mkdirs(path):
    try:
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        return True
    except:
        return False

'''
传入一个文件路径，文件不存在则创建
'''
def mkfile(path):
    try:
        if mkdirs(path):
            with open(path, 'a') as f:
                f.write("")
            f.close()
            return True
        else:
            return False

    except:
        return False

'''
判断文件是否存在
'''
def file_exists(path):
    try:
        return os.path.isfile(path)
    except:
        return False