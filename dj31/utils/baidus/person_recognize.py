# -*- encoding:utf-8 -*-
"""
@作者：leel
@文件名：person_recognize.py
@时间：2020/7/2  13:06
@文档说明:
"""
from aip import AipBodyAnalysis

""" 你的 APPID AK SK """
APP_ID = '20713199'
API_KEY = 'O9CzLlo3niKuVewjbVAu7YZD'
SECRET_KEY = 'G8kMInYh59fH1EomZaoIkvtEU7kx0ZzH'

client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('double.jpg')#注意识别不了动画图
#
# """ 调用人体检测与属性识别 """
# data = client.bodyAttr(image)
# dic1 = data['person_info'][0]['attributes']
# for i,j in dic1.items():
#     print(i,j['name'])

""" 读取图片 """#静态人物数量识别
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('0.jpg')

""" 调用人流量统计 """
data = client.bodyNum(image)
print(data)