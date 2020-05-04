#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models


class Category(models.Model):
    """Product category model"""
    name = models.CharField(unique=True, max_length=50, verbose_name='Nom')

    class Meta:
        verbose_name = 'Catégorie'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""
    name = models.CharField(
        unique=True, null=True, max_length=300, verbose_name='Nom')
    category_id = models.ForeignKey(
        Category, related_name='category',
        verbose_name='ID Catégorie', on_delete=models.CASCADE, null=True)
    store = models.CharField(
        max_length=300, verbose_name='Magasin(s)', blank=True)
    nutriscore = models.CharField(
        max_length=1, verbose_name='Nutriscore', blank=True)
    barcode = models.CharField(
        max_length=50, verbose_name='code-barre', blank=True)
    url = models.URLField(
        max_length=300, unique=True, null=True, verbose_name='URL')
    image = models.URLField(
        max_length=300, verbose_name='Photo', blank=True)

    lipids_for_100g = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Lipides', null=True)
    saturated_fats_for_100g = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Acides gras', null=True)
    sugars_for_100g = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Sucres', null=True)
    salt_for_100g = models.DecimalField(
        max_digits=4, decimal_places=2, verbose_name='Sel', null=True)

    class Meta:
        verbose_name = 'Produit'

    def __str__(self):
        return self.name
