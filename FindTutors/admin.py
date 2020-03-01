from django.contrib import admin

# Register your models here.
from .models import TUser, Request
#from .models import BigUser
# admin.site.register(BigUser)

admin.site.register(TUser)
admin.site.register(Request)