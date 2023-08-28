from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, UserProfile, Report


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    search_fields = ['title', 'content']
    list_display = ('title', 'slug', 'created_on', 'author')
    list_filter = ('author', 'created_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on')
    list_filter = ('author', 'created_on', 'post')
    search_fields = ('author', 'body', 'post')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'first_name', 'last_name', 'about')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_item', 'reason', 'timestamp')
    list_filter = ('reason', 'timestamp')
    search_fields = ('reporter__username', 'reported_item__title', 'reason')


admin.site.register(Report, ReportAdmin)
