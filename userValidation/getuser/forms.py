from django import forms


class SignUp(forms.Form):
    name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=40, required=True)
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()
