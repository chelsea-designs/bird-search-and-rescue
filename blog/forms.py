from django import forms
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class BlogPostForm(forms.ModelForm):
    '''
    form to add blog posts
    '''
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'image_url',
            'image',
            'content',
        )
        widgets = {
            'content': SummernoteWidget(),
        }

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)