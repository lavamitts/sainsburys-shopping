import json
import os
import re
import utils.utils as u
from datetime import timedelta


class Recipe(object):
    def __init__(self, cell, menu_date):
        self.cell = cell
        self.menu_date = menu_date
        self.recipe_date = self.menu_date

        # These variables are needed in menu.py
        self.day_index = 0
        self.recipe = ""
        self.source = ""
        a = 1

    def parse(self):
        self.get_day_of_week()
        self.get_tea_recipe()
        self.remove_unnecessary_properties()
        a = 1

    def get_day_of_week(self):
        days = {
            "saturday": 0,
            "sunday": 1,
            "monday": 2,
            "tuesday": 3,
            "wednesday": 4,
            "thursday": 5,
            "friday": 6,
        }
        parts = [part.strip() for part in self.cell.split("\n")]
        a = 1

        matches = [(part, day) for part in parts for day in days if day in part.lower()]

        if matches:
            for part, day in matches:
                day_index = days[day]
                self.recipe_date = self.menu_date + timedelta(days=day_index)
                break

    def get_tea_recipe(self):
        parts = [part.strip() for part in self.cell.split("\n")]
        matches = [part for part in parts if "tea:" in part.lower()]
        if matches:
            txt = matches[0]
            parts = [part.strip() for part in txt.split("\t")]
            recipe_string = parts[-1]
            self.source = u.extract_text_in_parentheses(recipe_string)
            if self.source != None:
                self.source = re.sub(r"p\.? [0-9]+", "", self.source).strip()
                self.source = re.sub(r"p\.?[0-9]+", "", self.source).strip()
            if "(" in recipe_string:
                self.recipe = u.left_of_char(recipe_string, "(").strip()
            else:
                self.recipe = recipe_string.strip()

        self.correct_typos()

    def correct_typos(self):
        self.recipe = self.recipe.lower().capitalize().strip()
        config_folder = u.make_or_get_directory("resources", "config")
        replacements_file = os.path.join(config_folder, "replacements.json")
        if os.path.exists(replacements_file):
            with open(replacements_file) as replacements_file:
                replacements = json.load(replacements_file)
                for key in replacements:
                    replacement = replacements[key]
                    self.recipe = re.sub(key, replacement, self.recipe)
                    if self.source is not None:
                        self.source = re.sub(key, replacement, self.source)
                a = 1

    def remove_unnecessary_properties(self):
        del self.cell
        del self.menu_date
