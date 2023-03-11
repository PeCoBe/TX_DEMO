import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from yaml_analyzer import *
import pytest
import yaml

def test_add_missing_fields_P(load_file):
    current = {"foo": "bar", "baz": {"qux": 42}}
    new = {"foo": "bar", "baz": {"qux": 42, "quux": "corge"}, "grault": "garply"}
    expected = {"foo": "bar", "baz": {"qux": 42, "quux": "corge"}, "grault": "garply"}

    add_missing_fields(current, new)

    assert current == expected

# def test_add_missing_fields_N(load_file):
#     (current, new, expected) = load_file
#     add_missing_fields(current, new)
#     assert 'success' not in current
