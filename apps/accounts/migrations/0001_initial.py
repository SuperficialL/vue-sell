# Generated by Django 2.1.7 on 2019-04-17 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
                ('count', models.IntegerField(default=0, verbose_name='网站访问次数')),
            ],
            options={
                'verbose_name': '网站日访问量统计',
                'verbose_name_plural': '网站日访问量统计',
            },
        ),
        migrations.CreateModel(
            name='UserIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=30, verbose_name='IP地址')),
                ('ip_addr', models.CharField(default='', max_length=30, verbose_name='IP地理位置')),
                ('end_point', models.CharField(default='/', max_length=100, verbose_name='访问端点')),
                ('count', models.IntegerField(default=0, verbose_name='访问次数')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='最后访问时间')),
            ],
            options={
                'verbose_name': '访问用户信息',
                'verbose_name_plural': '访问用户信息',
            },
        ),
    ]
