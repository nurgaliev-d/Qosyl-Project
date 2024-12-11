from django.contrib import admin
# Register your models here.

from .models import  User,Topic

admin.site.register(User)
admin.site.register(Topic)
