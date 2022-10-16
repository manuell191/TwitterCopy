from django.shortcuts import render
from django.views.generic import ListView
from .models import User, Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

class UserList(ListView):
    model = User
    template_name = 'user_list.html'