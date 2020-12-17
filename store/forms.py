from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
      username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'User Name','class': 'form-control'}), required=True)
      email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'form-control'}), required=True)
      password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}), required=True)
      password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'form-control'}), required=True)

      class Meta:
          model = User
          fields = ['username', 'email', 'password1', 'password2']