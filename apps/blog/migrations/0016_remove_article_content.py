# Generated by Django 2.0.1 on 2019-04-02 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190402_2354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
