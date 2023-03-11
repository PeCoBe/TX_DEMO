import pytest
import yaml
import logging
import sys
import os

@pytest.fixture
def load_file():
    path_to = 'tests/scenario1'
    # Path for the current and new version files
    current_version_path = os.path.join(path_to, "current_version.yaml")
    new_version_path = os.path.join(path_to, "new_version.yaml")
    expected_version_path = os.path.join(path_to, "expected_version.yaml")

    # load the yaml files
    try:
        with open(current_version_path, encoding='utf-8') as file:
            current_version = yaml.load(file, Loader=yaml.FullLoader)
        with open(new_version_path, encoding='utf-8') as file:
            new_version = yaml.load(file, Loader=yaml.FullLoader)
        with open(expected_version_path, encoding='utf-8') as file:
            expected_version = yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        logging.error("File not found")
        sys.exit(1)
    except Exception as e:
        logging.error('Error loading current version: %s, e')
        sys.exit(1)

    versions = (current_version, new_version, expected_version)

    return versions
