# Generated by Django 2.0.1 on 2019-04-03 00:35

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True),
        ),
    ]
