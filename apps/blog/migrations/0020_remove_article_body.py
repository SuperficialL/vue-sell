# Generated by Django 2.0.1 on 2019-04-03 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_article_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
    ]
