from django.contrib import admin
from .models import Comment


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'article_id', 'created_time', 'parent_id', 'browser', 'ip_addr')
