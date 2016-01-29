# -*- coding: utf-8 -*-
from django import template
from store import settings
import datetime
from clothing.models import *
register = template.Library()


@register.filter()
def cutout(string):
    """
    截取前面一段字符,并在最后加上...
    """
@register.filter()
def price(id):
    """
    返回商品的第一个sku的价格
    """
    p = GoodSku.objects.filter(good_id=id)[0]
    return p.new_price

@register.filter()
def size(p):
    """
    返回商品的所有sku的尺寸
    参数是一个商品对象
    """
    sizelist = []
    sizestr = ''
    for sku in p.goodsku_set.all():
        if not sku.size.name in sizelist:
            sizelist.append(sku.size.name)

    for s in sizelist:
        sizestr += '<li>%s</li>' % s

    return sizestr

@register.filter()
def color(p):
    """
    返回商品的所有sku的尺寸
    参数是一个商品对象
    """
    colorlist = []
    colorstr = ''
    for sku in p.goodsku_set.all():
        if not sku.color.name in colorlist:
            colorlist.append(sku.color.name)

    for s in colorlist:
        colorstr += '<li>%s</li>' % s

    return colorstr


@register.inclusion_tag('include/product_block.html')
def product(p):
    """
    包含标签用来输出单个商品的展示块(主图,商品名,价格,销量)
    """
    MEDIA_URL = settings.MEDIA_URL
    # p = Good.objects.get(id=pid)
    return {'p': p, 'MEDIA_URL': MEDIA_URL}


@register.inclusion_tag('include/product_detail.html')
def product_detail(p):
    """
    包含标签用来输出单个商品图片框
    """
    MEDIA_URL = settings.MEDIA_URL
    return {'p': p, 'MEDIA_URL': MEDIA_URL}
"""
extras.py

from django import template
from blogapp.models import BlogPost

register = template.Library()

@register.inclusion_tag('bp_by_time.html')  # 通过修饰器注册inclution tag。
def bp_by_time(n):
    bps = BlogPost.objects.order_by('-timestamp')[:n]
    return {'bps': bps}
++++++++++++++++++++++

bp_by_time.html  标签的模板

{% autoescape off %}
{% for bp in bps %}
题目: <a href="/post/?BlogPost_id={{ bp.id }}">{{ bp.title }}</a><br>
作者: {{ bp.author }}<br>
正文: {{ bp.body }}<br>
创建时间: {{ bp.timestamp }}<br>
修改时间: {{ bp.last_modify_time }}
<hr>
{% endfor %}
{% endautoescape %}
+++++++++++++++++++++++++

index.html

{% extends "base.html" %}
{% load extras %}  # 加载标签
{% block content %}
<h1>这是首页,欢迎访问我的网站!这个网站基于django!</h1>
<div>
{% bp_by_time 4 %} # 调用标签渲染页面局部
</div>
{% endblock %}
+++++++++++++++++++++++++++




"""