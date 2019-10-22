from django.contrib import admin
from .models import User

class User_ad(admin.ModelAdmin):
    list_display=['Username','Email','Password']

admin.site.register(User,User_ad)
