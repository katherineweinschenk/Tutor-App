from django.contrib import admin

# Register your models here.
from .models import BigUser, Request

admin.site.register(BigUser)
admin.site.register(Request)