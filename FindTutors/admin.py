from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from .models import TUser, Request, Profile, Room, Reviews
#from .models import BigUser
# admin.site.register(BigUser)

admin.site.register(TUser)
admin.site.register(Request)
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Reviews)

class RequestAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

