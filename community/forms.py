from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from django import forms
from .models import Comment, Post, UserProfile


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profile_picture', 'first_name', 'last_name', 'about')
