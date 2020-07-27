from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Product)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('journalist','label','publish_date_byus','title','category','country','state')
admin.site.register(News,NewsAdmin)
