from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'created_on', 'author')
    list_filter = ('author', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('author', 'created_on')
    search_fields = ('author', 'body')
