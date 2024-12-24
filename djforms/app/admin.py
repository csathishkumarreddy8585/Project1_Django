from django.contrib import admin

# Register your models here.

from app.models import *

admin.site.register(Topic)
admin.site.register(Web_page)
admin.site.register(Access_Record)

