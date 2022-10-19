from django import forms
from django import forms

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['bio'].widget.attrs.update({
            'autocomplete': 'off'
        })
    
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(label='Bio')
    