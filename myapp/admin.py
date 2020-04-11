from django.contrib import admin
from django.apps import AppConfig
from .models import animal
from .models import Pics
from .models import vaccine
from django import template
from myapp import templates
register = template.Library()
# Register your models here.

@admin.register(animal)
@admin.register(vaccine)
#@admin.register(Pics)

class animal_admin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['sex']
    #list_filter=['']



#class animalAdminConfig(AppConfig):
#    name = 'animal_admin'

#class vaccineAdmin(admin.ModelAdmin):
#    list_display =['name']
