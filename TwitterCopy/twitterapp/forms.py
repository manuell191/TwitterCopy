from django import forms
from .models import User, Post

class UserCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autocomplete': 'off'
        })
    class Meta:
        model = User
        fields = '__all__'

class PostCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'autocomplete': 'off'
        })

    class Meta:
        model = Post
        fields = '__all__'