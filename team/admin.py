from django.contrib import admin
from .models import TeamMember


# Register your models here.
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'biography',
        'image',
    )

    ordering = ('name',)


admin.site.register(TeamMember, TeamMemberAdmin)
