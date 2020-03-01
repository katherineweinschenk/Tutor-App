from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .models import Request, TUser
#from .models import BigUser
from .forms import RequestForm, RegisterForm
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView

class TutorRegisterView(CreateView):
    model = TUser
    #form_class = RegisterForm               # check form
    fields = ['firstname', 'lastname', 'email', 'subjects', 'year', ]
    template_name = 'FindTutors/tutor_signup.html' # correct form HTML

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_tutor = True
        user.save()
        return redirect('/home/tutors/') # Go back to the table of tutors
        #return redirect('dashboard')           # redirect to proper dashboard

class TuteeRegisterView(CreateView):
    model = TUser
    # form_class = RegisterForm               # check form
    fields = ['firstname','lastname','email','subjects','year',]
    template_name = 'FindTutors/tutee_signup.html' # correct form HTML

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_tutee = True
        user.save()
        return redirect('/home/tutees/')  # Go back to the table of tutors
        # login(self.request, user)

        #return redirect('dashboard')           # redirect to proper dashboard

def Tutors(request):
    model = TUser
    #the_tutors = []
    the_tutors = TUser.objects.filter(is_tutor = True)
    # for user in BigUser.objects.all()
    #     if user.is_tutor:
    #         the_tutors.append(user)
    #         print(user)
    return render(request,'FindTutors/tutors.html',{'tutors':the_tutors})

def Tutees(request):
    all_tutees = TUser.objects.filter(is_tutee=True)

    return render(request, 'FindTutors/tutees.html', {'tutees': all_tutees})



#registration views
class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'


# class SignUpAsTutor(generic.TemplateView):
#     template_name = 'registration/signup.html'
#     redirect('tutor_dashboard')
#
# class SignUpAsTutee(generic.TemplateView):
#     template_name = 'registration/signup.html'
#     redirect('tutee_dashboard')
    
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

#def Dashboard(request):
 #   model = BigUser
  #  allUsers = BigUser.objects.all()
   # return render(request,'dashboard.html', {'all:': allUsers})

