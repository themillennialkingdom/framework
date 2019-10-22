from django import forms
from .models import User

class Signup_form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'