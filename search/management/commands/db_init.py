#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-23
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.core.management.base import BaseCommand, CommandError

from .database import Database
import requests

NUTRISCORE_FR = ["a", "b", "c", "d", "e"]
STDOUT = True


class Command(BaseCommand):
    """Command class for custom django commands"""
    help = "Load datas from the OFF API to our database"

    def add_arguments(self, parser):
        """ new argument """
        parser.add_argument("-n", "--nutriscore", type=str)
        parser.add_argument("-c", "--category", type=str)

    def handle(self, *args, **options):
        """Requests the API then fills the DB"""
        if not isinstance(options["category"], str):
            raise TypeError("Entrez une chaine de caractère.")

        if options["nutriscore"] not in NUTRISCORE_FR:
            raise TypeError("Entrez un nutriscore correct.")

        if options["category"] and options["nutriscore"]:
            category = options["category"]
            nutriscore = options["nutriscore"]
            
            self.db = Database()
            self.db.add_categories()
            self.db.add_products()
