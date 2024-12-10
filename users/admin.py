from django.contrib import admin

# Register your models here.

from .models import  User,Topic,MyChats

admin.site.register(User)
admin.site.register(Topic)
@admin.register(MyChats)
class MyChatsAdmin(admin.ModelAdmin):
    list_display = ('id','me','frnd','chats')
