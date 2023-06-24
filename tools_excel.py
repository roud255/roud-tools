import re
import os
import xlwt

'''
解析日志文件并输出到excel文件
'''
'''
此处示例丰网近两天打单数据整理，其他自行修改后使用
'''

path = ""  # 日志文件路径
book = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建excel文件
sheet = book.add_sheet('丰网打单数据', cell_overwrite_ok=True)  # 创建sheet
col = ['日期时间','单号', '寄件人手机', '收件人手机']  # 列名
count = 0
for i in range(len(col)):
    sheet.write(0, i, col[i])  # 写入列名


count = 1
with open(path,'r',encoding='utf-8') as f:
    for line in f:
        dan = re.findall(r'\|(.*?)\|\{"bigFon', line)
        shijian = (line.split("|"))[0]
        danhao = (dan[0].split("|"))[-1]
        arr = re.findall(r'mobile\"\:\"(.*?)\"', line)
        shoujian = (re.findall(r'mobile\"\:\"(.*?)\"', line))[0]
        jijian = (re.findall(r'mobile\"\:\"(.*?)\"', line))[1]
        arr2 = []
        arr2.append(shijian)
        arr2.append(danhao)
        arr2.append(jijian)
        arr2.append(shoujian)
        for i in range(len(arr2)):
            sheet.write(count, i, arr2[i])
        count += 1
        print(shijian+'  '+danhao+"  "+shoujian+"  "+jijian)

savepath = './丰网近两天打单数据.xls'
book.save(savepath)
print(count)
