from django import forms
from .models import User, Post

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'