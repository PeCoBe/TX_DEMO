import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from yaml_analyzer import *
import pytest
import yaml

def test_update_values_P():
    current = {'a': 1, 'b': {'c': 2, 'd': 3}}
    new = {'a': 4, 'b': {'c': 5, 'd': 6}}
    update_values(current, new)
    assert current == {'a': 4, 'b': {'c': 5, 'd': 6}}

def test_update_values_N():
    current = {'a': 1, 'b': {'c': 2, 'd': 3}}
    new = {'a': 4, 'b': {'c': 'invalid'}}
    try:
        update_values(current, new)
    except TypeError:
        pass
    else:
        assert True, 'TypeError was not raised'
        #assert False, 'TypeError was not raised'
