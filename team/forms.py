from django import forms
from .models import TeamMember
from django_summernote.widgets import SummernoteWidget
from .widgets import CustomClearableFileInput


class TeamMemberForm(forms.ModelForm):
    '''
    form to add team member
    '''
    class Meta:
        model = TeamMember
        fields = (
            'name',
            'image_url',
            'image',
            'biography',
        )
        widgets = {
            'biography': SummernoteWidget(),
        }

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)