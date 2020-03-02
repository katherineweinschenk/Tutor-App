from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import BigUser, Request, Chat, TUser
from .forms import TutorUserSignUpForm, TuteeUserSignUpForm, RequestForm, RegisterForm
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
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

    # def get(self, request, *args, **kwargs):
    #     self.request_input.recipient = request.GET.get('recipient')
    #     return render(request, self.template_name, {'form': form})
    
    def form_valid(self, form):
        self.request_input = form.save(commit=False)
        self.request_input.sender = self.request.user
        self.request_input.recipient = TUser.objects.get(email=self.request.GET.get('recipient'))
        self.request_input.save()
        return redirect('/home/request/tutor_request/')


def TutorRequest(request):
    model = TUser
    all_tutors = TUser.objects.filter(is_tutor = True)
    if request.user.is_authenticated:
        print('pie')
    return render(request,'FindTutors/tutor_request.html', {'tutors':all_tutors})

#def Dashboard(request):
 #   model = BigUser
  #  allUsers = BigUser.objects.all()
   # return render(request,'dashboard.html', {'all:': allUsers})


def MessagesView(request):
    c = Chat.objects.all()
    return render(request, "FindTutors/messages.html", {'home': 'active', 'chat': c})


def Post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)

        c = Chat(user=request.user, message=msg)

        if msg != '':
            c.save()
        # mg = src="https://scontent-ord1-1.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/p160x160/11070096_10204126647988048_6580328996672664529_n.jpg?oh=f9b916e359cd7de9871d8d8e0a269e3d&oe=576F6F12"
        return JsonResponse({'msg': msg, 'user': c.user.username})
    else:
        return HttpResponse('Request must be POST.')

def GetMessages(request):
    c = Chat.objects.all()
    return render(request, 'FindTutors/messages.html', {'chat': c})
