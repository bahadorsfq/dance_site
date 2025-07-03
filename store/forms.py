from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="نام کاربری",
        widget=forms.TextInput(attrs={'placeholder': 'مثلاً: sara_dancer'})
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={'placeholder': 'مثلاً: you@example.com'})
    )
    password1 = forms.CharField(
        label="رمز عبور",
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور دلخواه'})
    )
    password2 = forms.CharField(
        label="تکرار رمز عبور",
        widget=forms.PasswordInput(attrs={'placeholder': 'دوباره رمز عبور'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

