from django import forms
from .models import NewsPost
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class NewsPostForm(forms.ModelForm):
    '''
    form to add news posts
    '''
    class Meta:
        model = NewsPost
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
