from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView)
from .models import  Account
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListaiView(LoginRequiredMixin, ListView):
    template_name = 'pages/home.html'
    model=Account

def DetailView(request, pk):
    account = Account.objects.get(pk=pk)
    
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "pages/detail.html", {"account": account})