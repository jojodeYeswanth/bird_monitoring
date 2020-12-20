from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bird
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password", "class": "form-control"}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password check", "class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddBirdForm(ModelForm):
    bird_name = forms.CharField(label="Enter Bird Name ")
    bird_type = forms.CharField(label="Enter Bird Type ")
    bird_gender = forms.CharField(label="Enter Bird Gender ")
    bird_color = forms.CharField(label="Enter Bird Color ")

    class Meta:
        model = Bird
        fields = ('bird_type', 'bird_name', 'bird_gender', 'bird_color')


class AddCageForm(ModelForm):
    cage_num = forms.CharField(label="Enter Cage Number ")
    bird_name = forms.ModelChoiceField(queryset=Bird.objects.all())

    class Meta:
        model = Bird
        fields = ('cage_num',)
