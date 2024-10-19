from django.contrib import admin
from .models import UserProfile, Organization, Product, Publication, Comment

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Publication)


class PublicationAdmin(admin.ModelAdmin):
  pass


class CommentAdmin(admin.ModelAdmin):
  pass

class OrganizationAdmin(admin.ModelAdmin):
  pass

admin.site.unregister(Publication)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Organization, OrganizationAdmin)