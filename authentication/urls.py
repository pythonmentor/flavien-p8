#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LogInForm

app_name = 'authentication'

urlpatterns = [
    path('', LoginView.as_view(authentication_form=LogInForm), name="login"),
    path('deconnexion/', LogoutView.as_view(), name="logout"),
    path('inscription/', views.SignUp.as_view(), name="signup"),
    path('profil/', views.profile, name="profile"),
]
