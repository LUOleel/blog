# -*- encoding:utf-8 -*-
"""
@作者：leel
@文件名：character_recognize.py
@时间：2020/7/2  12:27
@文档说明:
"""
import re
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID='20711349'
API_KEY = '	ErkKG3QtmuMWvrG1o9q3MVQz'
SECRET_KEY = 'YxG1xekcAC2xD0FnV1GWEo2FuLnydGWI'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('example.jpg')

""" 调用通用文字识别（含位置信息版）, 图片参数为本地图片 """
data = client.general(image)
print(data)

data = str(data)
pattern = re.compile("'words': '(.*?)'}")#:后有一个空格
res = pattern.findall(data)

for line in res:
    print(line)