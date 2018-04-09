from django.contrib import admin
from .models import *
# Register your models here.

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','phone', 'img')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'actor', 'img')

class CarrerAdmin(admin.ModelAdmin):
    list_display = ('id', 'actor', 'year', 'content')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'actor', 'video')

admin.site.register(Actor, ActorAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Carrer, CarrerAdmin)
admin.site.register(Video, VideoAdmin)
