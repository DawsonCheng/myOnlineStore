from django.contrib import admin
from netstoreapp.models import UserProfile,Classify,Commodity

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Classify)
admin.site.register(Commodity)