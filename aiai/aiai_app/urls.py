from . import views
from django.urls import path

urlpatterns = [
      path('', views.AccountRegistration.as_view(), name='register'),
]