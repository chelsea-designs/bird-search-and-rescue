from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import NewsPost


# Register your models here.
class NewsPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


admin.site.register(NewsPost, NewsPostAdmin)