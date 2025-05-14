from django.contrib import admin
from app.models import *


class WebpageAdmin(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['name']
    list_editable=['email']
    list_per_page=2
    search_fields=['name','url']
    list_filter=['url','name','email','topic_name']


class Access_RecordAdmin(admin.ModelAdmin):
    list_display=['name','author','date']
    list_display_links=['author']
    list_editable=('name',)
    list_per_page=2
    search_fields=['name','date']
    list_filter=['date','name',]


# Register your models here.
admin.site.register(Topic)
admin.site.register(Web_page,WebpageAdmin)
admin.site.register(Access_Record,Access_RecordAdmin)