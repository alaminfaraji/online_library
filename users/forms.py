from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class ChangeUserData(UserChangeForm):
    password=None
    class Meta:
        model = User
        fields=['username','email' ]
        
class DepositForm(forms.Form):
    amount = forms.DecimalField(label='Deposit Amount', max_digits=10, decimal_places=2)