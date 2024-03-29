from django import forms

class RegForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    # name = forms.CharField() # <Для аутентификации с помощью сессий (НЕ встроенной в Django)>

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password = forms.CharField(label="Password", widget=forms.PasswordInput())