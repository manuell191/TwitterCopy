from django import forms
from django import forms

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
    
    username = forms.CharField(label='Username')
    password = forms.CharField(widget=forms.PasswordInput())

class CreateUserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
        self.fields['bio'].widget.attrs.update({
            'autocomplete': 'off'
        })

    username = forms.CharField(label='Username')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Password again')
    bio = forms.CharField(label='User Bio (optional)', required=False)

class CreatePostForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'autocomplete': 'off'
        })

    content = forms.CharField(label='Content')