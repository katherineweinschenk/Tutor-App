from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout


class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'
    
class redirectView(generic.TemplateView):
    template_name = 'registration/redirect.html'

#@login_required
class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'