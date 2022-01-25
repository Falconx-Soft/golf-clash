import site
from django.contrib import admin
from .models import*
# Register your models here.

admin.site.register(ClubType)
admin.site.register(Club)
admin.site.register(BallPower)
admin.site.register(ClubLevel)