#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-18
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .forms import SignUpForm


class SignUp(FormView):
    """Show the form and create a user if its a valid one"""

    template_name = 'registration/account_creation.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        """if the form is validated"""

        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        if user:
            login(self.request, user)
        return super().form_valid(form)


def profile(request):
    """User profile"""

    return render(request, "registration/user_profile.html")
