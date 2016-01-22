# -*- coding: utf-8 -*-
from store import settings


def global_setting(request):

    MEDIA = settings.MEDIA_URL  # 媒体路径
    #
    # category_list = Category.objects.all()  # 分类信息
    # # 男装分类信息
    # category_list_m = [c for c in category_list if c.sex == 0]
    # # 女装分类信息
    # category_list_f = [c for c in category_list if c.sex == 1]
    # # 品牌信息
    # brand_list = Brand.objects.all()
    # # 热销榜
    # hot_list = Good.objects.all().order_by('-sales')[:4]
    # # 标签
    # tag_list = Tag.objects.all()
    return locals()