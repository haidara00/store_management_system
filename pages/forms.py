from django.contrib.auth import get_user_model
from django.forms import ModelForm
from allauth.account.views import SignupForm

class UserCreateForm(ModelForm):
    
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name","email", "password")