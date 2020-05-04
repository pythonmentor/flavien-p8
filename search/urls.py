#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-23
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.ProductSearchView.as_view(), name="search"),
    path('details/<int:pk>', views.ProductDetailsView.as_view(),
         name="product-details"),
]
