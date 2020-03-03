from django.urls import path
from . import views
from SuperTuber import settings
from django.conf.urls.static import static

app_name = 'FindTutors'

urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='signup'),
    #path('dashboard/', views.Dashboard, name='dashboard'),
    path('tutors/', views.Tutors, name='tutors'),
    path('tutees/', views.Tutees, name='tutees'),
    path('messages/', views.MessagesView.as_view(), name = 'messages'),
    path('request/', views.RequestView.as_view(), name='request'),
    path('register_tutor/', views.TutorRegisterView.as_view(), name='tutor_register'),
    path('register_tutee/', views.TuteeRegisterView.as_view(), name='tutee_register'),
    path('request/tutor_request/', views.TutorRequest, name='tutor_request' ),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.editprofile, name='edit_profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)