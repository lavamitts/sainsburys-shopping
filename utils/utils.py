from datetime import datetime
from pathlib import Path
import os
import re


def extract_text_in_parentheses(text):
    match = re.search(r'\((.*?)\)', text)  # Find text inside parentheses
    return match.group(1) if match else None  # Return the text if found


def left_of_char(text, char):
    return text.split(char, 1)[0] if char in text else text


def find_docx_files(root_folder):
    return [
        str(file) for file in Path(root_folder).rglob("*.docx")
        if "template" not in file.stem.lower()
        and "$" not in file.stem.lower()
    ]


def clear_screen():
    if os.name == 'nt':  # For Windows
        _ = os.system('cls')
    else:  # For Mac and Linux
        _ = os.system('clear')


def make_or_get_directory(*folders):
    """
    Ensures a nested folder structure exists within the current working directory.

    Args:
        *folders: A sequence of folder names, where each is a child of the previous one.

    Returns:
        str: The final full path of the deepest folder.
    """
    current_path = os.getcwd()  # Get the current working directory

    for folder in folders:
        current_path = os.path.join(current_path, folder)  # Build the path
        os.makedirs(current_path, exist_ok=True)  # Create folder if it doesn't exist

    return current_path  # Return the final directory path


def validate_date_code(code: str) -> bool:
    """
    Validate a date code in YYMMDD format.
    Example: '250915' -> 2025-09-15

    Returns True if valid, False if not.
    """
    if len(code) != 6 or not code.isdigit():
        return False

    try:
        year = 2000 + int(code[0:2])   # assume 2000–2099
        month = int(code[2:4])
        day = int(code[4:6])

        datetime(year, month, day)  # will raise ValueError if invalid
        return True
    except ValueError:
        return False
