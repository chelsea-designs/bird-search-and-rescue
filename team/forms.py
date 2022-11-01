from django import forms
from .models import TeamMember
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

    image = forms.ImageField(
                             label='Image',
                             required=False,
                             widget=CustomClearableFileInput)
