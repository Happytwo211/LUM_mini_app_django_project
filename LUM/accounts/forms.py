from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from allauth.account.forms import SignupForm

class SighUpForm(UserCreationForm):
    # email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    # last_name = forms.CharField(label="Фамилия")
    phone_number = forms.Field()
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            # "last_name",
            # "email",
            "password1",
            "password2",
        )

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        try:
            user.groups.add(common_users)
            return user
        except Exception as e:
            print('Произошла ошибка'
                  f'\n{e}')