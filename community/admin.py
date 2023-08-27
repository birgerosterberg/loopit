from django.contrib import admin
from .models import Post, Comment, UserProfile, Report
from django_summernote.admin import SummernoteModelAdmin


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
    # Define the fields you want to display in the admin list view
    list_display = ('user', 'profile_picture',
                    'first_name', 'last_name', 'about')


class ReportAdmin(admin.ModelAdmin):
    list_display = ('reporter', 'reported_item', 'reason', 'timestamp')
    list_filter = ('reason', 'timestamp')
    search_fields = ('reporter__username', 'reported_item__title', 'reason')


admin.site.register(Report, ReportAdmin)
