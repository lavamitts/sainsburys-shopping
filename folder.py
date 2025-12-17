from classes.environment_variable import EnvironmentVariable
from datetime import datetime
import os
import subprocess


# Get the document save path
shopping_folder = EnvironmentVariable("shopping_folder", "string", False).value
current_year = str(datetime.now().year)
output_path = os.path.join(str(shopping_folder), current_year)

subprocess.run(["open", output_path])
