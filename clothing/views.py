# coding=utf-8

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from models import Ad, Category, Brand, Good, Tag
# Create your views here.
from store import settings


def global_setting(request):
    MEDIA_URL = settings.MEDIA_URL  # 媒体路径
    ADS = Ad.objects.all()  # 广告
    CATEGORY = Category.objects.all()  # 分类信息
    BRAND = Brand.objects.all()  # 品牌信息
    BRAND_MAN = BRAND.filter(sex=1).values('name').distinct()  # 男式品牌
    BRAND_WOMAN = BRAND.filter(sex=0).values('name').distinct()  # 女式品牌
    NEW = Good.objects.all().order_by('-pk')[:10]  # 最新商品
    HOT = Good.objects.all().order_by('-sales_month')[:10]  # 最新商品
    TAG = Tag.objects.all()  # 标签

    return locals()


def index(request):
    return render(request, "index.html", locals())  # 这个可以使用上下文管理器中的变量.
    # return render_to_response('index.html', locals(), context_instance=RequestContext(request))  # 这个方法也可以正常使用
    # return render_to_response('index.html', locals())  # 这个方法不能正常使用,因为不能用到上下文管理器中的变量.


def products(request):
    # 得到商品id
    try:
        pid = request.GET.get('pid', None)
        try:
            p = Good.objects.get(pk=pid)    # 查询到商品对象
        except Good.DoesNotExist:
            return render(request, 'error.html', {"reason": "商品不存在"})
    except Exception as e:
        print e
        # logger.error(e)

    return render(request, 'products.html', locals())

#
# def detail(request, id):
#     p = Good.objects.get(id=id)
#     return render(request, '')


def brand(request):
    # 得到品牌bid,得到性别sex
    try:
        bid = request.GET.get('bid', None)
        try:
            b = Brand.objects.get(pk=bid)
        except Brand.DoesNotExist:
            return render(request, 'error.html', {"reason": "品牌不存在"})
    except Exception as e:
        print e
        # logger.error(e)
    return None