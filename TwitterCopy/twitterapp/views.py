from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import User, Post
from .forms import PostCreateForm, UserCreateForm

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
    return redirect('userlist')

class PostList(ListView):
    model = Post
    template_name = 'post_list.html'

class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm

def PostDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('postlist')

def UserProfile(request, pk):
    query = Post.objects.filter(user=pk)
    user = User.objects.get(id=pk)
    context = {
        "post_list": query,
        "user": user
    }
    return render(request, 'user_profile.html', context)

def UserUpdate(request, pk):
    if request.method == "POST":
        form =  UserCreateForm(request.POST)
        if form.is_valid:
            user = User.objects.get(id=pk)
            user.username = request.POST["username"]
            user.bio = request.POST["bio"]
            user.save()
            return redirect('userlist')
    else:
        form = UserCreateForm
    return render(request, 'user_update.html', {"form": form})