#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-30
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.db import IntegrityError
from django.urls import reverse

from save.models import Favorites
from search.models import Category, Product
from authentication.models import User


def db_init():
    """Create a temp user and temp products to perform tests"""
    user = User.objects.create(email='remy@purbeurre.fr')
    user.set_password('pixar2020')
    user.save()

    data = Category(name="Pate à tartiner")
    data.save()

    data = Product(
        name="Beurre de cacahuètes",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Carrefour",
        nutriscore="c",
        barcode="012456870000",
        url="https://peanutbutter.fr",
        image="https://peanutbutter.fr/photo.jpg",
        lipids_for_100g="2.60",
        saturated_fats_for_100g="0.59",
        sugars_for_100g="0.11",
        salt_for_100g="3.51",
    )
    data.save()

    data = Product(
        name="Ovomaltine",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Leclerc, BioCoop",
        nutriscore="a",
        barcode="0189654870000",
        url="https://ovomaltine.fr",
        image="https://ovomaltine.fr/photo.jpg",
        lipids_for_100g="4.59",
        saturated_fats_for_100g="0.02",
        sugars_for_100g="1.54",
        salt_for_100g="3.25",
    )
    data.save()

    data = Product(
        name="Nutella",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Auchan",
        nutriscore="c",
        barcode="012232370000",
        url="https://nutella.fr",
        image="https://nutella.fr/photo.jpg",
        lipids_for_100g="1.64",
        saturated_fats_for_100g="0.33",
        sugars_for_100g="2.20",
        salt_for_100g="1.06",
    )
    data.save()


class TestSaveFavorites(TestCase):
    """To test the favorites functionalities"""
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.favorites_url = reverse('save:favorites')
        cls.save_url = reverse('save:save')
        db_init()

    def test_favorites_page_returns_200(self):     # checking FavoritesView()
        """To test the status code and the login page"""
        response = self.client.get(self.favorites_url)
        self.assertTemplateUsed(response, 'save/favorites.html')
        self.assertEqual(response.status_code, 200)

    def test_favorites_page_without_any_saving_yet(self):
        """To check the favorites page doesn't contains products when no one is already saved"""
        self.client.login(username='remy@purbeurre.fr',
                          password='pixar2020')
        user_id = User.objects.get(email='remy@purbeurre.fr').id
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.context_data["object_list"].count(), 0)

    def test_favorites_page_with_a_saved_product(self):
        """To check the favorites page prints a product when it's saved"""
        self.client.login(
            username='remy@purbeurre.fr',
            password='pixar2020')

        user_id = User.objects.get(email='remy@purbeurre.fr').id
        response = self.client.post(
            self.save_url, {
                'original_product_id': Product.objects.get(id=1).id,
                'substitute_id': Product.objects.get(id=2).id,
                'user_id': user_id,
                'next': '/',
            }
        )
        response = self.client.get(self.favorites_url)
        self.assertEqual(response.context_data["object_list"].count(), 1)
        self.assertEqual(response.status_code, 200)

    def test_favorites_with_one_saved_product(self):
        """To check the favorites response when a product is saved"""
        self.client.login(
            username='remy@purbeurre.fr',
            password='pixar2020')

        user_id = User.objects.get(email='remy@purbeurre.fr').id
        response = self.client.post(
            self.save_url, {
                'original_product_id': Product.objects.get(id=1).id,
                'substitute_id': Product.objects.get(id=2).id,
                'user_id': user_id,
                'next': '/',
            }
        )
        self.assertEqual(Favorites.objects.all().count(), 1)
        self.assertRedirects(   # check the redirection to the favorites page
            response, '/save/favorites/',
            status_code=302, target_status_code=200)
