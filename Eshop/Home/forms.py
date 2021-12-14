from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import ContactUs
from django.contrib.auth.models import User

user = get_user_model()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email :', widget=forms.TextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(label='Username :', widget=forms.TextInput(attrs={'placeholder':'Username'}))
#    first_name = forms.CharField(label='First Name :', widget=forms.TextInput(attrs={'placeholder':'First Name'}))
#    last_name = forms.CharField(label='Last Name :', widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
    class Meta():
        model = user
        fields = ['username', 'email', 'password1']

class ContactUsForm(forms.ModelForm):
    email = forms.EmailField(label='Email:', widget=forms.TextInput(attrs={'placeholder':'Email Addresse'}))
    msg = forms.CharField(label='Message:', widget=forms.Textarea(attrs={'placeholder':'Enter Your Probleme'}))
    username = forms.CharField(label='Username:', widget=forms.TextInput(attrs={'placeholder':'Username'}))
    class Meta():
        model = ContactUs
        fields = ['email', 'username', 'msg']
