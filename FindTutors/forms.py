from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import TUser, Profile, Request, Reviews
from django.forms import ModelForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms import bootstrap
from django.utils.translation import gettext_lazy as _
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'description', 'location',)

# Creating a Central Registration Form that will work for both Tutor and Tutee (set Booleans in view)
class RegisterForm(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'email', 'phone_number',)


class TutorUserSignUpForm(forms.ModelForm):
    class Meta:
        model = TUser #change model to TutorProfile and add bio
        fields = ['username','firstname', 'lastname', 'email', 'phone_number', 'subjects', 'year', 'image', 'bio' ]
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'phone_number': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'subjects': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


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


#TutorRegistrationForm
class TutorRegistration(UserCreationForm):
    class Meta:
        model = TUser
        fields = ('firstname', 'lastname', 'phone_number', 'subjects')


#update user profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'year', 'user_type', 'subjects', 'bio']

class ReviewRatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['profile', 'rating', 'reviews']

