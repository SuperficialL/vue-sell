# Generated by Django 2.2 on 2019-04-03 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_article_format_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notice',
            old_name='info',
            new_name='text',
        ),
    ]
