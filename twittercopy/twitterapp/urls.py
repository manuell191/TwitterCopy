from importlib.resources import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),
    path('user/list', views.userList, name='userlist'),
    path('user/profile/<pk>', views.userProfile, name='userprofile'),
    path('post/list', views.postList, name='postlist'),
    path('post/create', views.postCreate, name='postcreate'),
    path('post/delete/confirm/<pk>', views.postDeleteConfirm, name='postdeleteconfirm'),
    path('post/detele/<pk>', views.postDelete, name='postdelete'),
    path('user/update/<pk>', views.userUpdate, name='userupdate'),
    path('user/password/update/<pk>', views.passwordUpdate, name='passwordupdate'),
    path('user/delete/confirm/<pk>', views.userDeleteConfirm, name='userdeleteconfirm'),
    path('user/delete/<pk>', views.userDelete, name='userdelete')
]