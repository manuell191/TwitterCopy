from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import User, Post
from .forms import UserCreateForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

class UserList(ListView):
    model = User
    template_name = 'user_list.html'

class UserCreate(CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = UserCreateForm

def UserDelete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('home')