from datetime import datetime, date, timedelta
from pathlib import Path
import os
import re
import sys
import termios
import tty
from typing import Any, Optional, List, Union


def clear_cell(cell: Any) -> None:
    """Remove all paragraphs from a table cell."""
    cell_element: Any = cell._element
    for p in cell.paragraphs:
        para_element: Any = p._element
        cell_element.remove(para_element)


def next_saturday():
    today = date.today()
    # weekday(): Monday=0 ... Sunday=6
    days_ahead = (5 - today.weekday()) % 7
    if days_ahead == 0:  # If today is Saturday, go to next week
        days_ahead = 7
    next_sat = today + timedelta(days=days_ahead)
    return next_sat.strftime("%y%m%d")


def extract_text_in_parentheses(text: str) -> Optional[str]:
    """
    Extract the first substring inside parentheses from a string.

    Args:
        text (str): The input string.

    Returns:
        Optional[str]: The text inside the first pair of parentheses,
                       or None if no parentheses are found.
    """
    match = re.search(r"\((.*?)\)", text)
    return match.group(1) if match else None


def left_of_char(text: str, char: str) -> str:
    """
    Return the substring of `text` to the left of the first occurrence of `char`.
    If `char` is not in `text`, return the full string.

    Args:
        text (str): The input string.
        char (str): The character or substring to split on.

    Returns:
        str: Substring to the left of `char`, or the full string if not found.
    """
    return text.split(char, 1)[0] if char in text else text


def find_docx_files(root_folder: Union[str, Path]) -> List[str]:
    """
    Recursively find all .docx files in the given folder, excluding templates
    and temporary files.

    Args:
        root_folder (str | Path): The root folder to search.

    Returns:
        List[str]: List of .docx file paths as strings.
    """
    root_path = Path(root_folder)
    return [str(file) for file in root_path.rglob("*.docx") if "template" not in file.stem.lower() and "$" not in file.stem.lower()]


def clear_screen():
    if os.name == "nt":  # For Windows
        _ = os.system("cls")
    else:  # For Mac and Linux
        _ = os.system("clear")


def make_or_get_directory(*folders: str) -> str:
    """
    Ensures a nested folder structure exists within the current working directory.

    Args:
        *folders: A sequence of folder names, where each is a child of the previous one.

    Returns:
        str: The final full path of the deepest folder.
    """
    current_path: str = os.getcwd()  # Get the current working directory

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
        year = 2000 + int(code[0:2])  # assume 2000–2099
        month = int(code[2:4])
        day = int(code[4:6])

        datetime(year, month, day)  # will raise ValueError if invalid
        return True
    except ValueError:
        return False


def getch():
    """Read a single character from stdin without pressing Enter."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
