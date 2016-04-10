from django.contrib import admin
from netstoreapp.models import UserProfile,Classify,Commodity,Cart

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Classify)
admin.site.register(Commodity)
admin.site.register(Cart)