from django.contrib import admin
from django.contrib.admin.sites import site
from blog.models import Post
# Register your models here.

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyinject.js',)
