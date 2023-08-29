from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from django import forms
from .models import Comment, Post, UserProfile, Report

# Define a form for creating and updating Comments


class CommentForm(forms.ModelForm):
    """
    A form for handling the creation and updating of Comment instances.
    """
    class Meta:
        # The model to use for the form
        model = Comment

        # The fields to include in the form
        fields = ('body',)

# Define a form for creating and updating Posts


class PostForm(forms.ModelForm):
    """
    A form for handling the creation and updating of Post instances.
    """
    class Meta:
        # The model to use for the form
        model = Post

        # The fields to include in the form
        fields = ('title', 'content', 'category')

        # Using SummernoteWidget for the 'content'
        # field for a rich text editing experience.
        widgets = {
            'content': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and its helper.
        """
        super().__init__(*args, **kwargs)
        # Using crispy_forms to improve form rendering
        self.helper = FormHelper()

# Define a form for creating and updating UserProfiles


class UserProfileForm(forms.ModelForm):
    """
    A form for handling the creation and updating of UserProfile instances.
    """
    class Meta:
        # The model to use for the form
        model = UserProfile
        # The fields to include in the form
        fields = ('profile_picture', 'first_name', 'last_name',
                  'about')

# Define a form for creating and updating Reports


class ReportForm(forms.ModelForm):
    """
    A form for handling the creation and updating of Report instances.
    """
    class Meta:
        # The model to use for the form
        model = Report
        # The fields to include in the form
        fields = ['reason']
