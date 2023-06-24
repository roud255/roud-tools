import os
import uuid

import requests
from tools_file import mkfile, mkdirs

'''
下载网页中的ts文件并拼接成mp4输出
'''

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

ts_savepath = "D:/Download/pycharm_roud_media/ts_file/"
tstxt_savepath = "D:/Download/pycharm_roud_media/ts_txt/ts.txt"
#遍历url下载ts
def download(a, b, baseurl):
    for i in range(a,b):
        #这里自行拼接ts的url
        var_uri = str(i)+".ts"

        #根据变量拼接ts下载链接
        base_url = baseurl+var_uri
        ts_data = requests.get(url=base_url,headers=headers).content
        mkdirs(ts_savepath+"1.ts")
        save_path = ts_savepath + var_uri
        with open(save_path, "wb") as f1:
            f1.write(ts_data)
            f1.close()
            print(save_path + "保存完成")
        mkfile()
        with open(tstxt_savepath, "a") as f2:
            s = "file \'" + save_path + "\'\n"
            f2.write(s)
            f2.close()

#部分ts文件为空，需要重新下载
def download_retry(a, b, baseurl):
    for i in range(a, b):
        # 这里自行拼接ts的url
        var_uri = str(i) + ".ts"

        # 根据变量拼接ts下载链接
        base_url = baseurl + var_uri
        try:
            ts_data = requests.get(url=base_url, headers=headers,timeout=5).content
            mkdirs(ts_savepath + "1.ts")
            save_path = ts_savepath + var_uri
            with open(save_path, "wb") as f1:
                f1.write(ts_data)
                f1.close()
                print(save_path + "保存完成")
        except:
            pass

#判断ts文件是否为空，为空则重新下载
def download_retry_auto(a, b, prefix, suffix, baseurl):
    print("检查空文件并重试下载...")
    flag = 0
    for i in range(a, b):
        mkfile(prefix+str(i)+suffix)
        size = os.path.getsize(prefix+str(i)+suffix)
        if(size == 0):
            download_retry(i, i+1, baseurl)
            flag+=1
    if flag == 0:
        return False
    else:
        return True

def ts_2_mp4():
    name = uuid.uuid4()
    mkdirs(tstxt_savepath)
    #加r才不会被转义，一般用于正则
    #拼接ts文件的ffmpeg命令，自行修改路径
    com = r'ffmpeg -f concat -safe 0 -i D:/Download/pycharm_roud_media/ts_txt/ts.txt -c copy D:/Download/pycharm_roud_media/video/{}.mp4'.format(name)
    os.system(com)
    os.remove(tstxt_savepath)

def main(a, b, u):
    download(a, b, u)
    flag = True
    while(flag):
        flag = download_retry_auto(a, b, "D:/Download/pycharm_roud_media/ts_file/", ".ts", u)
    ts_2_mp4()
    print("完成")