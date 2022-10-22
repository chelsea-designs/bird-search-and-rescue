from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TeamMember


# Register your models here.
class TeamMemberAdmin(SummernoteModelAdmin):
    summernote_fields = ('biography',)


admin.site.register(TeamMember, TeamMemberAdmin)