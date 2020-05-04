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
    """Create a few temp products to perform tests"""
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


class TestSaveSubstitution(TestCase):
    """To test the subs and saving functionalities"""
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.sub_url = reverse('save:substitution')
        cls.save_url = reverse('save:save')
        cls.favorites_url = reverse('save:favorites')
        db_init()

    def test_substitution_page_returns_200(self):     # checking SubstitutionView()
        """To test the status code and the login page"""
        response = self.client.get('/save/substitution/1')
        self.assertTemplateUsed(response, 'save/substitution.html')
        self.assertEqual(response.status_code, 200)

    def test_substitution_only_get_products_with_better_nutriscore(self):
        """To check if we get products better than the selected one"""
        response = self.client.get('/save/substitution/1')
        # careful here, we also take the products with the same nutriscore
        self.assertEqual(response.context_data["object_list"].count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_substitution_no_better_nutriscore(self):
        """To check if we get zero product when there is no better one"""
        response = self.client.get('/save/substitution/2')
        self.assertEqual(response.context_data["object_list"].count(), 0)
        self.assertEqual(response.status_code, 200)

    def test_substitution_context_data(self):
        """To check if the context method gets the right elements"""
        response = self.client.get('/save/substitution/1')
        self.assertEqual(response.status_code, 200)
        product = Product.objects.get(id=1)
        self.assertEqual(response.context_data["name"], product.name)
        self.assertEqual(response.context_data["id"], product.id)
        self.assertEqual(response.context_data["image"], product.image)

    def test_substitution_unknown_id(self):
        """To check the redirection if there's actually no product"""
        response = self.client.get('/save/substitution/15')
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    