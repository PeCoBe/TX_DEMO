import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from yaml_analyzer import *
import pytest
import yaml

def test_merge_fields_P():
    # Testing a positive scenario where new fields are merged into the current dictionary
    current = {'a': 1, 'b': {'c': 2}}
    new = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    merge_fields(current, new)
    assert current == expected

def test_merge_fields_P():
    # Testing a negative scenario where current file is not empty
    current = {'a': 1, 'b': {'c': 2}}
    new = {'b': {'d': 3}, 'e': 4}
    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    merge_fields(current, new)
    assert current != new
    assert current != 0