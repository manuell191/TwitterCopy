from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import LoginForm, CreateUserForm, CreatePostForm
from .models import Profile, Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerPage(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            bio = request.POST.get('bio')

            if password1 != password2:
                messages.error(request, 'Passwords do not match')
            
            User.objects.create_user(username=username, password=password1)
            user = User.objects.get(username=username)
            profile = Profile(user=user, bio=bio)
            profile.save()

            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('home')
    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
        
    context = {'page': page, 'form': LoginForm}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

#the only cbv because it's so simple
class UserList(ListView):
    model = User
    template_name = 'user_list.html'

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    profile = Profile.objects.get(user=user)
    query = Post.objects.all()
    context = {
        'profile': profile,
        'post_list': query
    }
    return render(request, 'user_profile.html', context)

def postList(request):
    query = Post.objects.all()
    context = {'post_list': query}
    return render(request, 'post_list.html', context)

@login_required
def postCreate(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            user = request.user
            author = Profile.objects.get(user=user)

            post = Post(author=author, content=content)
            post.save()

            return redirect('postlist')
    form = CreatePostForm()
    context = {'form': form}
    return render(request, 'post_create.html', context)

@login_required
def postDeleteConfirm(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'post_delete.html', context)

@login_required
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('postlist')