#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-30
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models

from search.models import Product
from app_purbeurre.settings import AUTH_USER_MODEL


class Favorites(models.Model):
    """Set the Favorites model"""
    original_product_id = models.ForeignKey(
        Product,
        related_name='original',
        on_delete=models.CASCADE
    )
    substitute_id = models.ForeignKey(
        Product,
        related_name='substitute',
        on_delete=models.CASCADE
    )

    user_id = models.ForeignKey(
        AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['original_product_id', 'substitute_id', 'user_id'],
                name='unique_relation')
        ]
        verbose_name = "Favoris"
