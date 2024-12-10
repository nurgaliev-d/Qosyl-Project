from django.contrib import admin
from .models import ActivityLog
# Register your models here.

from .models import  User,Topic

admin.site.register(User)
admin.site.register(Topic)

class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'hours_spent')