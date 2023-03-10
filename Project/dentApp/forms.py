# from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth.models import User
from .models import Contact


# this is for login of patient 
# class LoginForm(AuthenticationForm):
#     username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))



# this is for signup of patient
class PatientRegistrationForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget = forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# this is for contact us 
class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']



# this is for Appointment form 
