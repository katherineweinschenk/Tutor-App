# from django.contrib import admin
# from django.urls import path
# from FindTutors import views
# from django.conf.urls import include
# from django.contrib.auth import views as auth_views
#
# urlpatterns = [
#     path('home/', include('FindTutors.urls')),
#     path('admin/', admin.site.urls),
#     path('home/', views.HomeView.as_view(), name='home'),
#     path('', views.SignUpView.as_view(), name='signup'),
#     path('', include('social_django.urls', namespace='social')),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
#     path('complete/google-oauth2/home/', views.redirectView.as_view(), name='redirect'),
# ]
#
#
# from django.urls import path
# from django.conf.urls import url
#
# from . import views
# from SuperTuber import settings
# from django.conf.urls.static import static
#
# app_name = 'FindTutors'
#
# urlpatterns = [
#     path('register/', views.SignUpView.as_view(), name='signup'),
#     #path('dashboard/', views.Dashboard, name='dashboard'),
#     path('tutors/', views.Tutors, name='tutors'),
#     path('tutees/', views.Tutees, name='tutees'),
#     path('request/', views.RequestView.as_view(), name='request'),
#     path('tutor_registration/', views.TutorRegistrationView.as_view(),
#          name='tutor_registration'),
#     path('register_tutor/', views.TutorRegisterView.as_view(), name='tutor_register'),
#     path('register_tutee/', views.TuteeRegisterView.as_view(), name='tutee_register'),
#     path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
#     path('profile/', views.ProfileView.as_view(), name='profile'),
#     path('profile/edit', views.editprofile, name='edit_profile'),
#     path('request/tutor_request/', views.TutorRequest, name='tutor_request'),
#     url(r'^messages/$', views.MessagesView.as_view(), name='messages'),
#     url(r'^post/$', views.Post, name='post'),
#     url(r'^GetMessages/$', views.GetMessages, name='GetMessages'),
#
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path
from FindTutors import views
from django.conf.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', include('FindTutors.urls')),
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(), name='home'),
    path('', views.SignUpView.as_view(), name='signup'),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('complete/google-oauth2/home/',
         views.redirectView.as_view(), name='redirect'),
]


