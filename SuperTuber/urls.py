from django.contrib import admin
from django.urls import path, include 
from FindTutors import views

urlpatterns = [
    path('home/', include('FindTutors.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/tutor/', views.TutorSignUpView.as_view(), name='tutor_signup'),
    path('accounts/signup/tutee/', views.TuteeSignUpView.as_view(), name='tutee_signup'),
]
