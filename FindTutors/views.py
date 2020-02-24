from django.views import generic
from .models import BigUser, Request
from .forms import TutorUserSignUpForm, TuteeUserSignUpForm, RequestForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponseRedirect

class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'

class MessagesView(generic.TemplateView):
    template_name = "FindTutors/messages.html"

class SignUpView(generic.CreateView):
    model = BigUser
    form_class = TutorUserSignUpForm
    template_name = 'Registration/signup_form.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = self.request.user.username
        # login(self.request, user)
        user.save()
        return redirect('/FindTutors/dashboard/')

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

def signup(request):
    return render(request, 'Registration/signup_form.html')

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