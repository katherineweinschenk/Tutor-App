from django.urls import path

from . import views

app_name = 'FindTutors'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('tutors/', views.Tutors, name='tutors'),
    path('request/', views.RequestView.as_view(), name='request'),
]