from importlib.resources import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('user/list', views.UserList.as_view(), name='userlist'),
    path('user/profile/<pk>', views.userProfile, name='userprofile')
]