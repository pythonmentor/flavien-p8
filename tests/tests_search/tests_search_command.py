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


class TestCommand(TransactionTestCase):
    """Tests the commands file to fill the database"""

    @patch("search.management.commands.db_init.STDOUT", new_callable=bool)
    def test_command_type_errors(self, mock):
        """To check the errors raises"""
        mock = False
        with self.assertRaises(TypeError):
            call_command("db_init", nutriscore="n")
        with self.assertRaises(TypeError):
            call_command("db_init", category=15)

    @patch("search.management.commands.db_init.requests.get")
    @patch("search.management.commands.db_init.STDOUT", new_callable=bool)
    def test_command_filling_the_database(self, mock, mock_json):
        """To check if the database is properly filled"""
        mock = False
        mock_json.return_value.json.return_value = {
            'products': [{
                'product_name_fr': 'Mock Produit 1',
                'stores': 'Magasin 1',
                'nutrition_grade_fr': ['a'],
                'code': '123456789',
                'image_url': 'https://image_produit_1.fr',
                'url': 'https://url_produit_1.fr',
                'nutriments': {
                    'salt_100g': '1.1',
                    'sugars_100g': '1.09',
                    'fat_100g': '22.15',
                    'saturated-fat_100g': '10.2',},
                },

                {
                'product_name_fr': 'Mock Produit 2',
                'stores': 'Magasin 2',
                'nutrition_grade_fr': ['a'],
                'code': '987654321',
                'image_url': 'https://image_produit_2.fr',
                'url': 'https://url_produit_2.fr',
                'nutriments': {
                    'salt_100g': '1.1',
                    'sugars_100g': '1.09',
                    'fat_100g': '22.15',
                    'saturated-fat_100g': '10.2',}
                },  
            ]
        }
        self.assertEqual(Product.objects.all().count(), 0)
        self.assertEqual(Category.objects.all().count(), 0)
        call_command("db_init", nutriscore="a", category="Pizzas")
        self.assertEqual(Product.objects.all().count(), 2)
        self.assertEqual(Category.objects.all().count(), 1)
        call_command("db_init", nutriscore="a", category="Pizzas")
        self.assertEqual(Product.objects.all().count(), 2)
        self.assertEqual(Category.objects.all().count(), 1)
