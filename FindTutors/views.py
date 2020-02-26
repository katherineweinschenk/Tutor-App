from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout


class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'
    

def logoutview(request):
    logout(request)
    return render(request, 'registration/signup.html')

#@login_required
class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'