import os
import pytest
import yaml


def test_current_version_not_found():
    result = os.system('python yaml_analyzer.py --path-to tests/scenario9')
    assert result == 257  # This will be the return code when rule4 and rule5 are set true at the same time
