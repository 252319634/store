# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'ad/', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
            ],
            options={
                'verbose_name': '\u5e7f\u544a',
                'verbose_name_plural': '\u5e7f\u544a',
            },
        ),
        migrations.CreateModel(
            name='Attr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': '\u5c5e\u6027',
                'verbose_name_plural': '\u5c5e\u6027',
            },
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x80\xbc')),
                ('attr', models.ForeignKey(verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x90\x8d', to='clothing.Attr')),
            ],
            options={
                'ordering': ('attr__name',),
                'verbose_name': '\u5c5e\u6027\u503c',
                'verbose_name_plural': '\u5c5e\u6027\u503c',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('index_my', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('selected', models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xbb\x93\xe7\xae\x97')),
            ],
            options={
                'verbose_name': '\u8d2d\u7269\u8f66',
                'verbose_name_plural': '\u8d2d\u7269\u8f66',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbb')),
                ('sex', models.SmallIntegerField(default=1, blank=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(1, b'\xe7\x94\xb7\xe5\xbc\x8f'), (0, b'\xe5\xa5\xb3\xe5\xbc\x8f')])),
                ('index_my', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('attrvalue', models.ManyToManyField(to='clothing.AttrValue', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe9\xa2\x9c\xe8\x89\xb2')),
            ],
            options={
                'verbose_name': '\u989c\u8272',
                'verbose_name_plural': '\u989c\u8272',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('sex', models.SmallIntegerField(default=1, blank=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(1, b'\xe7\x94\xb7\xe5\xbc\x8f'), (0, b'\xe5\xa5\xb3\xe5\xbc\x8f')])),
                ('desc_my', models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('details', tinymce.models.HTMLField(max_length=10000, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85')),
                ('image', models.ImageField(upload_to=b'%Y%m', null=True, verbose_name=b'\xe4\xb8\xbb\xe5\x9b\xbe', blank=True)),
                ('prices', models.CharField(default=b'0', max_length=20, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('nums', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('view', models.IntegerField(default=0, null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f')),
                ('attrvalue', models.ManyToManyField(to='clothing.AttrValue', verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7')),
                ('brand', models.ForeignKey(verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', to='clothing.Brand')),
                ('category', models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='clothing.Category')),
            ],
            options={
                'ordering': ['-view'],
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1',
            },
        ),
        migrations.CreateModel(
            name='GoodSku',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('artno', models.CharField(max_length=30, verbose_name=b'\xe8\xb4\xa7\xe5\x8f\xb7')),
                ('old_price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8e\x9f\xe4\xbb\xb7')),
                ('new_price', models.FloatField(default=0.0, verbose_name=b'\xe7\x8e\xb0\xe4\xbb\xb7')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('image', models.ImageField(upload_to=b'%Y%m', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True)),
                ('color', models.ForeignKey(verbose_name=b'\xe9\xa2\x9c\xe8\x89\xb2', to='clothing.Color')),
                ('good', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.Good')),
            ],
            options={
                'verbose_name': '\u5546\u54c1SKU',
                'verbose_name_plural': '\u5546\u54c1SKU',
            },
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.ImageField(upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('goodsku', models.ForeignKey(to='clothing.GoodSku')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('orderid', models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7')),
                ('time_my', models.DateTimeField(auto_now=True, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('address', models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe4\xbf\xa1\xe6\x81\xaf')),
                ('total_price', models.FloatField(default=0.0, null=True, verbose_name=b'\xe6\x80\xbb\xe9\x87\x91\xe9\xa2\x9d')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7')),
                ('goodsku', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.GoodSku')),
                ('order', models.ForeignKey(verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7', to='clothing.Order')),
            ],
            options={
                'verbose_name': '\u9500\u552e\u8bb0\u5f55',
                'verbose_name_plural': '\u9500\u552e\u8bb0\u5f55',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8')),
                ('index_my', models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u5c3a\u5bf8',
                'verbose_name_plural': '\u5c3a\u5bf8',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('recipients', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba', blank=True)),
                ('qq', models.CharField(default=b'', max_length=20, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('tel', models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True)),
                ('address', models.CharField(default=b'', max_length=200, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', blank=True)),
                ('view_history', models.CommaSeparatedIntegerField(default=b'', max_length=10, null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe8\xae\xb0\xe5\xbd\x95')),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goodsku',
            name='size',
            field=models.ForeignKey(verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8', to='clothing.Size'),
        ),
        migrations.AddField(
            model_name='good',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe', blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='goodsku',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.GoodSku'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ad',
            name='good',
            field=models.ForeignKey(to='clothing.Good'),
        ),
    ]
