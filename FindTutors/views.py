from django.views import generic
from .models import MyUser
from .forms import TuteeSignUpForm, TutorSignUpForm

class HomeView(generic.TemplateView):
    template_name = 'FindTutors/home.html'

class SignUpView(generic.TemplateView):
    template_name = 'registration/signup.html'

class TutorSignUpView(generic.CreateView):
    model = MyUser
    form_class = TutorSignUpForm
    template_name = 'registration/signup_form.html'

class TuteeSignUpView(generic.CreateView):
    model = MyUser
    form_class = TuteeSignUpForm
    template_name = 'registration/signup_form.html'
    