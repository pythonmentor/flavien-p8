#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-30
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.urls import path
from . import views

app_name = 'save'

urlpatterns = [
    path('substitution/<int:product_id>', views.SubstitutionView.as_view(),
         name="substitution"),
    path('save/', views.saving_product, name="save"),
    path('favorites/', views.FavoritesView.as_view(), name="favorites"),
]
