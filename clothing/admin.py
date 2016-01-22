# coding:utf-8
from django import forms
from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple
from clothing.models import *


class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline, ]


class AttrValueInline(admin.StackedInline):
    model = AttrValue
    extra = 1
    ordering = ('name',)

class AttrAdmin(admin.ModelAdmin):
    inlines = [AttrValueInline, ]


class ImgAdminInline(admin.StackedInline):
    model = Img
    # fk_name = 'good'
    extra = 0

class GoodSkuAdminInline(admin.StackedInline):

    model = GoodSku
    extra = 0
    readonly_fields = ('sc',)
    # fields = ('sc',)
    # filter_horizontal = ('image',)

class GoodAdmin(admin.ModelAdmin):
    inlines = [GoodSkuAdminInline]
    filter_horizontal = ('attrvalue',)
    # form = 'AttrValueForm'
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }  # 这个可用,这个字段变成了复选框形式



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Size)
admin.site.register(Tag)
admin.site.register(Img)
admin.site.register(Good, GoodAdmin)
admin.site.register(Attr, AttrAdmin)
admin.site.register(AttrValue)
admin.site.register(Color)
admin.site.register(Ad)
admin.site.register(Selling)
admin.site.register(Cat1)
admin.site.register(Cat2)