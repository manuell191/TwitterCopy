from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/list', views.UserList.as_view(), name='userlist')
]