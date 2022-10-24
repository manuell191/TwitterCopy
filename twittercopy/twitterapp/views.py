from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import LoginForm, CreateUserForm, CreatePostForm, UpdateUserForm, UpdatePasswordForm
from .models import Profile, Post

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
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
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')
        
    context = {'form': LoginForm}
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
    if request.user != post.author.user:
        return redirect('home')
    context = {'post': post}
    return render(request, 'post_delete.html', context)

@login_required
def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.author.user:
        return redirect('home')
    post.delete()
    return redirect('postlist')

@login_required
def userUpdate(request, pk):
    if request.method == 'POST':
        form =  UpdateUserForm(request.POST)
        if form.is_valid:
            username = request.POST.get('username')
            bio = request.POST.get('bio')

            user = User.objects.get(id=pk)
            user.username = username
            user.save()

            profile = Profile.objects.get(user=user)
            profile.bio = bio
            user.save()
            return redirect('userlist')
    user = User.objects.get(id=pk)
    if request.user != user:
        return redirect('home')
    form = UpdateUserForm()
    context = {'form': form}
    return render(request, 'user_update.html', context)

@login_required
def passwordUpdate(request, pk):
    if request.method == 'POST':
        form =  UpdatePasswordForm(request.POST)
        if form.is_valid:
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if password1 != password2:
                messages.error(request, 'Passwords do not match')
            
            user = User.objects.get(id=pk)
            username = user.username
            user.set_password(password1)
            user.save()

            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return redirect('userlist')
    user = User.objects.get(id=pk)
    if request.user != user:
        return redirect('home')

    form = UpdatePasswordForm()
    context = {'form': form,}
    return render(request, 'password_update.html', context)

@login_required
def userDeleteConfirm(request, pk):
    user = User.objects.get(id=pk)
    if request.user != user:
        return redirect('home')
    return render(request, 'user_delete.html')

@login_required
def userDelete(request, pk):
    user = User.objects.get(id=pk)
    if request.user != user:
        return redirect('home')
    user.delete()
    return redirect('home')