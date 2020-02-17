from django.views import generic
from .models import BigUser
from .forms import TutorUserSignUpForm, TuteeUserSignUpForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render

class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'


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

def signup(request):
    return render(request, 'Registration/signup_form.html')

def Dashboard(request):
    model = BigUser
    allUsers = BigUser.objects.all()
    return render(request,'dashboard.html', {'all:': allUsers})