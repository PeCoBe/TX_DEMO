import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from yaml_analyzer import *
import pytest
import yaml

def test_remove_extra_fields_P():
    # Testing a positive scenario where extra fields are removed from the current dictionary
    current = {'a': 1, 'b': {'c': 2}, 'd': 3}
    new = {'a': 1, 'b': {'c': 2}}
    expected = {'a': 1, 'b': {'c': 2}}
    remove_extra_fields(current, new)
    assert current == expected

def test_remove_extra_fields_N():
    # Testing a negative scenario where current are not removed
    current = {'a': 1, 'b': {'c': 2}, 'd': 3}
    new = {'a': 1, 'b': {'c': 2}}
    expected = {'a': 1, 'b': {'c': 2}, 'd': 3}
    merge_fields(current, new)
    assert current == expected