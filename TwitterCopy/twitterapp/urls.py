from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/list', views.UserList.as_view(), name='userlist'),
    path('user/create', views.UserCreate.as_view(), name='usercreate'),
    path('user/delete/<pk>', views.UserDelete, name='userdelete'),
    path('post/list', views.PostList.as_view(), name='postlist'),
    path('post/create', views.PostCreate.as_view(), name='postcreate'),
    path('post/delete/<pk>', views.PostDelete, name='postdelete'),
    path('user/profile/<pk>', views.UserProfile, name='userprofile'),
    path('user/update/<pk>', views.UserUpdate, name='userupdate')
]