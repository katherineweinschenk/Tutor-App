from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .models import BigUser, Request
from .forms import RequestForm
from django.shortcuts import redirect
from django.shortcuts import render

#registration views
class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'
    
class redirectView(generic.TemplateView):
    template_name = 'registration/redirect.html'

class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'

class MessagesView(generic.TemplateView):
    template_name = "FindTutors/messages.html"

class RequestView(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'FindTutors/request.html'
    recipient = None

    def get(self, request, *args, **kwargs):
        self.recipient = request.GET.get('recipient')
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    
    def form_valid(self, form):
        self.request_input = form.save(commit=False)
        self.request_input.sender = self.request.user
        self.request_input.recipient = self.recipient
        self.request_input.save()
        return redirect('/../home/')        

def Dashboard(request):
    model = BigUser
    allUsers = BigUser.objects.all()
    return render(request,'dashboard.html', {'all:': allUsers})

def Tutors(request):
    model = BigUser
    the_tutors = []
    for user in BigUser.objects.all():
        if user.is_tutor:
            the_tutors.append(user)
            print(user)
    return render(request,'FindTutors/tutors.html',{'tutors':the_tutors})
