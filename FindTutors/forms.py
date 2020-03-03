from django import forms
from django.contrib.auth.forms import UserCreationForm
# from .models import  BigUser, Request, TUser
from .models import TUser, Request, Profile
from django.forms import ModelForm
from django.contrib.auth.models import User

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'location',)

# Creating a Central Registration Form that will work for both Tutor and Tutee (set Booleans in view)
class RegisterForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)

class TutorUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number','year','subjects')
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_tutor = True
    #     if commit:
    #         user.save()
    #     return user

class TuteeUserSignUpForm(UserCreationForm):
    class Meta:
        model = TUser
        fields= ('firstname', 'lastname', 'email', 'phone_number','year','subjects')
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.is_tutee = True
    #     if commit:
    #         user.save()
    #     return user


#update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'year', 'user_type', 'subjects', 'bio']

