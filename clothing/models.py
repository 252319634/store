# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
import sys
from django.utils.timezone import now

reload(sys)
sys.setdefaultencoding("utf-8")
# UnicodeEncodeError
class UserProfile(models.Model):
    """
    用户类,扩展User
    """
    user = models.OneToOneField(User, primary_key=True)
    qq = models.CharField(max_length=20, default='', blank=True, verbose_name='QQ号码')
    tel = models.CharField(max_length=20, default='', blank=True, verbose_name='手机号码')
    address = models.CharField(max_length=200, default='', blank=True, verbose_name='地址')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Cart(models.Model):
    """
    购物车,衣服的列表
    """
    user = models.ForeignKey(User, verbose_name='用户')
    goods = models.ForeignKey('Good', verbose_name='商品')
    count = models.IntegerField(default=1, verbose_name='数量')

    def __str__(self):
        return "用户%s选购:%s,%s件" % (self.user.username, self.goods.name, self.count)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = '购物车'


class Selling(models.Model):
    """
    销售记录
    """
    good = models.ForeignKey('Good', verbose_name='商品')
    user = models.ForeignKey(User, verbose_name='用户')
    count = models.IntegerField(verbose_name='数量')
    price = models.FloatField(default=0.0, verbose_name='单价')

    def __str__(self):
        return "%s购买%s,数量%s个,单价%s" % (self.user.username, self.good.name, self.count, self.price)

    class Meta:
        verbose_name = '销售记录'
        verbose_name_plural = verbose_name


class Ad(models.Model):
    """
    广告图片轮播
    """
    img = models.ImageField(upload_to='ad/', blank=False, null=False, verbose_name='广告图片')
    good = models.ForeignKey('Good')

    def __str__(self):
        return "%s的广告图片" % self.good.name

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name


class Cat1(models.Model):
    """
    一级分类
    """
    name = models.CharField(max_length=20,blank=False,verbose_name='大类')
    sex = models.SmallIntegerField(choices=((1, '男式'), (0, '女式')), null=False, default=1, blank=True, verbose_name='性别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '一级分类'
        verbose_name_plural = '一级分类'



class Cat2(models.Model):
    """
    二级分类
    """
    name = models.CharField(max_length=20, blank=False, verbose_name='大类')
    father = models.ForeignKey('Cat1', verbose_name='所属大类')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '二级分类'
        verbose_name_plural = '二级分类'

class Category(models.Model):
    """
    商品分类
    """
    name = models.CharField(max_length=20, blank=False, verbose_name='商品分类')
    father = models.ForeignKey('Cat2', verbose_name='所属二级分类')
    # 男装,女装
    sex = models.SmallIntegerField(choices=((1, '男式'), (0, '女式')), null=False, default=1, blank=True, verbose_name='性别')
    index = models.SmallIntegerField(default=1, blank=False, verbose_name='排序')
    # 数字小的靠前

    def __str__(self):
        str = "男" if self.sex == 1 else "女"
        return str + "---" + self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Brand(models.Model):
    name = models.CharField(max_length=20, verbose_name='品牌')
    index = models.SmallIntegerField(default=1, verbose_name='排序')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Size(models.Model):
    name = models.CharField(max_length=20, verbose_name='尺寸')
    index = models.IntegerField(default=1, verbose_name='排列顺序')

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = verbose_name
        ordering = ['index', ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = '尺寸'


class Color(models.Model):
    name = models.CharField(max_length=10, verbose_name='颜色')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '颜色'
        verbose_name_plural = verbose_name


# 标签
class Tag(models.Model):
    name = models.CharField(max_length=30, verbose_name='标签')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Img(models.Model):
    """
    商品的图片,一个商品有多个图片
    """
    goodsku = models.ForeignKey('GoodSku', null=False)
    # good = models.ForeignKey('Good', null=False)
    url = models.ImageField('图片', upload_to='')
    # index = models.SmallIntegerField('排序')
    # uplaod_to是指定存储目录,主目录在settings.MEDIA_ROOT定义

    def __str__(self):
        return self.goodsku

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'


class Attr(models.Model):
    """
    属性列表,衣服的各种属性名称
    """
    name = models.CharField(max_length=20, verbose_name='属性名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '属性'
        verbose_name_plural = verbose_name
        ordering = ('name',)


class AttrValue(models.Model):
    """
    属性的值
    """
    attr = models.ForeignKey('Attr', verbose_name='属性名')
    name = models.CharField(max_length=30, verbose_name='属性值')

    def __str__(self):
        return "%s---%s" % (self.attr.name, self.name)

    class Meta:
        verbose_name = '属性值'
        verbose_name_plural = verbose_name
        ordering = ('attr__name',)  # 排序后方便选取属性


class GoodSku(models.Model):
    good = models.ForeignKey('Good', verbose_name='商品')
    size = models.ForeignKey(Size, verbose_name='尺寸')
    color = models.ForeignKey(Color, verbose_name='颜色')
    old_price = models.FloatField(default=0.0, verbose_name='原价')
    new_price = models.FloatField(default=0.0, verbose_name='现价')
    num = models.IntegerField(default=0, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    image = models.ImageField(upload_to='%Y%m', blank=True, null=True, verbose_name='图片')

    def sc(self):  # 计算字段要显示在修改页面中只能定义在只读字段中(否则不显示):readonly_fields = ('sc',)
        return '%s,%s' % (self.size.name, self.color.name)

    sc.short_description = '尺寸颜色'  # 用于显示时的名字 , 没有这个将显示'sc'
    # sc.short_scription = '尺寸颜色'  # 用于显示时的名字 , 没有这个将显示'sc'

    def __str__(self):
        return "%s %s %s" % (self.good.name, self.size.name, self.color.name)


class Good(models.Model):
    """
    衣服
    """
    category = models.ForeignKey(Category, verbose_name='分类')
    brand = models.ForeignKey(Brand, verbose_name='品牌')
    name = models.CharField(max_length=100, verbose_name='名称')
    artno = models.CharField(max_length=30, verbose_name='货号')
    attrvalue = models.ManyToManyField('AttrValue', verbose_name='属性')
    desc = models.CharField(max_length=100, verbose_name='简介')
    price = models.FloatField(default=0.0, verbose_name='价格')
    sales = models.IntegerField(default=0, verbose_name='销量')
    sales_month = models.IntegerField(default=0, verbose_name='本月销量')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='标签')
    image = models.ImageField(upload_to='%Y%m', blank=True, null=True, verbose_name='主图')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品'