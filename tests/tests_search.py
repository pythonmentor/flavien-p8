#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-24
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client, TransactionTestCase
from django.db import IntegrityError
from django.urls import reverse
from django.core.management import call_command
from unittest.mock import patch

from search.models import Category, Product


def db_init():
    """Create temp products to perform tests"""
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
        nutriscore="b",
        barcode="012232370000",
        url="https://nutella.fr",
        image="https://nutella.fr/photo.jpg",
        lipids_for_100g="1.64",
        saturated_fats_for_100g="0.33",
        sugars_for_100g="2.20",
        salt_for_100g="1.06",
    )
    data.save()


class TestSearch(TestCase):
    """To test the search app"""
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.search_url = reverse('search:search')
        db_init()

    def test_details_page_error_404_when_no_such_product(self):
        """To check the invalid response when there's no food"""
        response = self.client.get('/search/details/15')
        self.assertEqual(response.status_code, 404)

    def test_search_page_returns_200(self):     # checking ProductSearchView()
        """To test the status code and the search page"""
        response = self.client.get(self.search_url +"?query=food")
        self.assertTemplateUsed(response, 'search/search_results.html')
        self.assertEqual(response.status_code, 200)

    def test_search_page_error_404_when_invalid_url(self):
        response = self.client.get(self.search_url + "?query=Nutella&page=@")
        self.assertEqual(response.status_code, 404)

    def test_no_entry_to_search(self):
        "To check the redirection if empty form entry"
        response = self.client.get(self.search_url)
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)

    def test_searching_context(self):
        "To check the context query method"
        response = self.client.get(self.search_url + "?query=Nutella")
        self.assertEqual(response.context_data["search"], "Nutella")

    def test_search_is_valid(self):
        "To check if we find a product if it's there"
        response = self.client.get(self.search_url + "?query=Ovomaltine")
        self.assertEqual(response.context_data["object_list"].count(), 1)

    def test_no_product_available(self):
        "To check if we don't actually find any undesirable product"
        response = self.client.get(self.search_url + "?query=banane")
        self.assertEqual(response.context_data["object_list"].count(), 0)
