from . import login, views
from django.urls import path

urlpatterns = [
    path('login',login.Login,name='Login'),
    path("logout",login.Logout,name="Logout"),
    path('register',login.AccountRegistration.as_view(), name='register'),
    path('',login.home,name=""),

    path('home',views.ListaiView.as_view(), name='home'),
    path('home/<int:pk>',views.DetailView, name='detail'),
]