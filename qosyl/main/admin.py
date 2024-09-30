from django.contrib import admin
from .models import UserProfile, Organization, Product, Publication

admin.site.register(UserProfile)
admin.site.register(Organization)
admin.site.register(Product)
admin.site.register(Publication)
