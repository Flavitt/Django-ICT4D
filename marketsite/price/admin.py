from django.contrib import admin

from .models import Crop, Choice

class CropAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'crop_text', 'price']

admin.site.register(Crop, CropAdmin)

# Register your models here.

