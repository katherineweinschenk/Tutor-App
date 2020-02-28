from django.views import generic
from .models import BigUser, Request, Chat
from .forms import TutorUserSignUpForm, TuteeUserSignUpForm, RequestForm
from django.http import HttpResponse, JsonResponse
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

class RequestView(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'FindTutors/request.html'

    def form_valid(self, form):
        request_input = form.save(commit=False)
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

