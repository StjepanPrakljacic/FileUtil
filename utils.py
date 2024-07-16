###############################################################################
# FileUtil - Utility Functions
#
# Description: This module provides utility functions that support file and
#              directory operations, such as handling file paths and checking
#              file extensions.
#
# Created by: Stjepan Prakljačić
# License: MIT License
# Repository: https://github.com/StjepanPrakljacic/FileUtil
#
# Version: 1.0.0
###############################################################################
import os


def path_validation(path: str) -> bool:
    """
    Check if a given path exists.

    Args:
        path (str): The path to be validated.

    Returns:
        bool: True if the path exists, False otherwise.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' does not exist.")
    return True


def get_file_size(path: str):
    """
    Get the size of a file in bytes.

    Args:
        path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.

    Raises:
        FileNotFoundError: If the path does not exist.
    """
    path_validation(path)
    return os.path.getsize(path)


def file_extension_check(path: str) -> bool:
    """
    Check if the file at the given path has a valid extension.

    This function validates the given path to ensure it exists and then checks
    if the file has one of the predefined valid extensions.

    Args:
        path (str): The path to the file to be checked.

    Returns:
        bool: True if the file has a valid extension, False otherwise.

    Raises:
        FileNotFoundError: If the path does not exist.
    """
    path_validation(path)
    valid_extensions = [".txt", ".json", ".xml", ".ini", ".config", ".csv"]
    ext = os.path.splitext(path)[-1].lower()
    return ext in valid_extensions
