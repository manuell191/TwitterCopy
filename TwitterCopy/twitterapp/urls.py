from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/list', views.UserList.as_view(), name='userlist'),
    path('user/create', views.UserCreate.as_view(), name='usercreate'),
    path('user/delete/<pk>', views.UserDelete, name='userdelete')
]