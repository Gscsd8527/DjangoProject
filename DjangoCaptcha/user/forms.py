# forms.py
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=3)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput())
    captcha = CaptchaField()  # 验证码字段
