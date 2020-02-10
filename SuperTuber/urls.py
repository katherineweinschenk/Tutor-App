from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('FindTutors.urls')),
    path('admin/', admin.site.urls),
]
