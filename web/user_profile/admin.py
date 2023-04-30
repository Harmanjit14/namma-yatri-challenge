from django.contrib import admin
from .models import UserProfile
from .models import AutoDriver, AutoDriverLocation
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(AutoDriver)
admin.site.register(AutoDriverLocation)
