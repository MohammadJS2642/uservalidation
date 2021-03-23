from django import forms

from .models import GettingUserData

# this class use Form and you should implement all of you want
# class SignUp(forms.Form):
#     name = forms.CharField(max_length=200, help_text="name")
#     username = forms.CharField(
#         max_length=40, required=True, help_text="username")
#     email = forms.EmailField(required=True, help_text='email')
#     password = forms.PasswordInput()


class SignUpForm(forms.ModelForm):
    class Meta:
        model = GettingUserData
        fields = ['name', 'username', 'email', 'password', 'gender']
        # widgets = {
        #     'name': (attrs={'cols': 80, 'rows': 20}),
        # }

        # this is show label in aside of inputs
        labels = {
            'name': (''),
            'username': (''),
            'email': (''),
            'password': (''),
            'gender': (''),
        }

        # show help_texts
        # help_texts = {
        #     'name': ('Some useful help text.'),
        # }

        # this is show error_messages
        error_messages = {
            'name': {
                'max_length': ("This writer's name is too long.name sould be less than 200 characters"),
            },
            'username': {
                'max_length': ("This writer's name is too long.name sould be less than 50 characters"),
            },
            # 'email': {
            #     'max_length': ("This writer's name is too long.name sould be less than 200 characters"),
            # },
            'password': {
                'max_length': ("This writer's name is too long.name sould be less than 20 characters"),
            },
            'gender': {
                'max_length': ('set your gender!')
            },
        }
