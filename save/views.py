#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-30
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from search.models import Product
from .models import Favorites
from authentication.models import User


class SubstitutionView(ListView):
    """
    Displays a list of products to replace the selected one

    Arguments: ListView {class} -- generic listview

    Returns: products -- products with better nutriscore in the same category

    """
    model = Product
    paginate_by = 6
    template_name = 'save/substitution.html'

    def get_queryset(self):
        """Allows some products from the same category"""
        self._id = self.kwargs['product_id']
        self.product = Product.objects.get(pk=self._id)
        return Product.objects.filter(
            category_id=self.product.category_id).filter(
            nutriscore__lte=self.product.nutriscore).exclude(
            id=self._id).order_by('nutriscore')

    def get_context_data(self, **kwargs):
        """Returns the required fiels of each product"""
        context = super().get_context_data(**kwargs)
        context['name'] = self.product.name
        context['id'] = self.product.id
        context['image'] = self.product.image
        return context


@login_required
def saving_product(request):
    """Method to save products when user is logged in"""
    if request.method == 'POST':
        product = request.POST['original_product_id']
        substitute = request.POST['substitute_id']
        page = request.POST['next']

        user_product = Product.objects.get(pk=product)
        user_substitute = Product.objects.get(pk=substitute)
        _user = User.objects.get(pk=request.user.pk)

        if user_product and user_substitute and _user:
            obj, created = Favorites.objects.get_or_create(
                original_product_id=user_product,
                substitute_id=user_substitute,
                user_id=_user,
            )
            if created:
                return redirect('save:favorites')
            else:
                messages.add_message(
                    request,
                    messages.INFO,
                    'Ce produit est déjà dans vos favoris'
                )
                return redirect(page)

    return redirect('index')


class FavoritesView(ListView, LoginRequiredMixin):
    """Lists all the saved products for a particular user"""
    template_name = 'save/favorites.html'
    paginate_by = 6

    def get_queryset(self):
        return Favorites.objects.filter(
            user_id=self.request.user.id).order_by("original_product_id")
