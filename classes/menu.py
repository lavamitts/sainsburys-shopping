from datetime import datetime, date
import re
from docx import Document
from classes.recipe import Recipe


class Menu(object):
    def __init__(self, menu_file):
        self.menu_file = menu_file
        self.recipes = []
        self.get_menu_date()

    def get_menu_date(self):
        match = re.search(r'\s(\d{6})\s', self.menu_file)
        if match:
            self.menu_date_string = match.group(1) if match else None
            self.menu_date = datetime.strptime(self.menu_date_string, "%y%m%d")
            self.menu_date = self.menu_date.date()
        else:
            self.menu_date_string = None
            self.menu_date = None

    def analyse(self):
        doc = Document(self.menu_file)  # Open the Word document
        if not doc.tables:
            raise ValueError("No tables found in the document.")

        table = doc.tables[0]  # Get the first table
        cells = [cell.text.strip() for row in table.rows for cell in row.cells]  # Extract text from all cells
        cells = cells[:7]
        for cell in cells:
            recipe = Recipe(cell, self.menu_date)
            recipe.parse()
            if recipe.recipe not in ["Tea", "Tea:"]:
                self.recipes.append(recipe)
