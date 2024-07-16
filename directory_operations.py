###############################################################################
# FileUtil - Directory Operations
#
# Description: This module provides functions for performing directory
#              operations such as creating directories and listing files
#              and subdirectories.
#
# Created by: Stjepan Prakljačić
# License: MIT License
# Repository: https://github.com/StjepanPrakljacic/FileUtil
#
# Version: 1.0.0
###############################################################################
import os


def create_dirs(root_dir: str, *directories: str):
    """
    Creates new directories based on the root directory and the names of the
    desired new directories.

    Args:
        root_dir (str): The path to the root directory.
        *directories (str): Variable number of directory names.

    Returns:
        list: The paths to the created directories.
    """
    created_paths = list()

    for directory in directories:
        path = os.path.join(root_dir, directory)

        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory '{directory}' created at '{path}'")
        else:
            raise FileExistsError(f"Directory '{directory}' already exists " \
                                  f"at '{path}'")

        created_paths.append(path)

    return created_paths
