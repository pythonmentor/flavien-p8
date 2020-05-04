#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django import forms
from django.forms import EmailInput, TextInput, PasswordInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class SignUpForm(UserCreationForm):
    """User registration"""

    class Meta:
        """Define all the informations given to the user
        while he's registrating

        """
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'password1', 'password2', )

    email = forms.EmailField(
        label='Votre email',
        widget=EmailInput(attrs={'class': 'form-control'}),
        error_messages={'required': 'Email requis',
                        'invalid': 'Email non valide',
                        'unique': 'Email déjà utilisé'})

    first_name = forms.CharField(
        required=False, label="Votre prénom (facultatif)",
        widget=TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        required=False, label="Votre nom (facultatif)",
        widget=TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(
        label="Choisissez un mot de passe",
        widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(
        label="Confirmez votre mot de passe",
        widget=PasswordInput(attrs={'class': 'form-control'}))


class LogInForm(AuthenticationForm):
    """Define all the informations given during the user login"""
    username = forms.EmailField(
        label="Votre identifiant (email)",
        widget=EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label="Votre mot de passe",
        widget=PasswordInput(attrs={'class': 'form-control'}))
