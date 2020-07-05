import logging

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from dj31.utils.captcha.captcha import captcha
from django_redis import get_redis_connection
# 导入日志器
logger = logging.getLogger('django')

def demo(request):
    return render(request,'news/index.html')

def register(request):
    return render(request,'users/register.html')

def image_code(request,img_id):
    text,image = captcha.generate_captcha()
    con_redis = get_redis_connection('verify_code')#连接用来存储图形验证码的redis1库
    img_key = "img_{}".format(img_id).encode('utf-8')#redis数据库时键值形式存储的
    # 将图片验证码的key和验证码文本保存到redis中，并设置过期时间
    con_redis.setex(img_key, 60, text)
    logger.info("图形验证码是: {}".format(text))
    return HttpResponse(content=image,content_type='image/jpg')
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)

