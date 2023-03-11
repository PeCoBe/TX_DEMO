# Import needed modules
import yaml
import os
import copy
import argparse
import logging
import sys

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--rule4', action='store_true', help='appy rule4')
parser.add_argument('--rule5', action='store_true', help='appy rule5')
parser.add_argument('--log-level', type=str, default='WARNING', help='Set the log level')
parser.add_argument('--path-to', type=str, default='', help='Set the path to file')
args, unknown = parser.parse_known_args()

# Set default level to WARNING
log_level = getattr(logging, args.log_level.upper())
logging.basicConfig(level=log_level)

# Set path to files
path_to = args.path_to

# Path for the current and new version files
current_version_path = os.path.join(path_to, "current_version.yaml")
new_version_path = os.path.join(path_to, "new_version.yaml")

# load the yaml files
try:
    with open(current_version_path, encoding='utf-8') as file:
        current_version = yaml.load(file, Loader=yaml.FullLoader)
    with open(new_version_path, encoding='utf-8') as file:
        new_version = yaml.load(file, Loader=yaml.FullLoader)
except FileNotFoundError:
    logging.error("File not found")
    sys.exit(257)
except TypeError as e:
    logging.error("Incorrect Format")
    sys.exit(258)
except Exception as e:
    logging.error('Error loading YAML file: %s', e)
    sys.exit(1)

# Rule 1: Add missing fields from new_version to current_version
def add_missing_fields(current, new):
    for key, value in new.items():
        if key not in current:
            current[key] = value
            # Info log
            logging.info('Adding new field with value: \n%s: %s', key, value)
        elif isinstance(value, dict):
            add_missing_fields(current[key], value)

# Rule 2: Keep value from current version
def merge_fields(current, new):
    for key, value in new.items():
        if key in current:
            if isinstance(current[key], dict) and isinstance(value, dict):
                merge_fields(current[key], value)
            else:
                # Info log
                logging.info('Keeping field and value: \n%s: %s', key, value)
                current[key] = current[key]
        else:
            # Info log
            logging.info('Updating field and value: \n%s: %s', key, value)
            current[key] = value

# Rule 3: Remove fields from current_version that are not present in new_version
def remove_extra_fields(current, new):
    for key in list(current.keys()):
        if key not in new:
            # Info log
            logging.info('Removed field in current_version: \n%s', key)
            del current[key]
        elif isinstance(current[key], dict) and isinstance(new[key], dict):
            remove_extra_fields(current[key], new[key])

# Rule 4: Update values of existing fields in both files
def update_values(current, new):
    for key, value in new.items():
        if key in current:
            if isinstance(current[key], dict) and isinstance(value, dict):
                update_values(current[key], value)
            else:
                # Info log
                logging.info('Updating value in current_version: \n%s: %s', key, value)
                current[key] = value

# create deep copies of the dictionaries
current_version_copy = copy.deepcopy(current_version)
new_version_copy = copy.deepcopy(new_version)

# Set rules based on arguments
rule4 = args.rule4
rule5 = args.rule5

# Check if both rules are selected, not allowed.
if rule4 and rule5:
    logging.critical('Cannot use flags Rule 4 and Rule 5 at the same time.')
    sys.exit(256)
elif rule4:
    # Apply rule 4, to only update existing fields.
    update_values(current_version_copy, new_version)
else:
    # update current_version_copy with missing fields from new_version_copy
    add_missing_fields(current_version_copy, new_version_copy)

    if rule5:
        # Rule 5: replace current_version with new_version values
        current_version_copy = new_version_copy
    else:
        # merge fields from new_version_copy to current_version_copy
        merge_fields(current_version_copy, new_version_copy)

        # remove extra fields from current_version_copy that are not present in new_version_copy
        remove_extra_fields(current_version_copy, new_version_copy)

# print the contents of the yaml files and updated current version
logging.debug('Current version: \n%s', current_version)
logging.debug('New version: \n%s', new_version)
logging.debug('########')
logging.debug('Updated current version (rule4=%s, rule5=%s):\n%s', rule4, rule5, current_version_copy)

# Updating current_version.yaml
try:
    with open(current_version_path, 'w', encoding='#utf-8') as file:
        logging.info("Updating current version...")
        current_version = yaml.dump(current_version_copy, file, allow_unicode=True, sort_keys=False, default_flow_style=False)
        logging.info('Current version updated! ありがとう~! (￣︶￣)')
        print('Current version updated! ありがとう~! (￣︶￣)')
except FileNotFoundError:
    logging.error("File not found")
    sys.exit(1)
except Exception as e:
    logging.error('Error loading current version: %s', e)
    sys.exit(1)