from . import views
from django.urls import path

urlpatterns = [
    path('',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path("home",views.home,name="home"),
]