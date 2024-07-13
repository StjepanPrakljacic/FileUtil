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
    if os.path.exists(path):
        return True
    return False