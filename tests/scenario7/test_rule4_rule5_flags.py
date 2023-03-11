import os
import pytest
import yaml


def test_rule4_and_rule5():
    result = os.system('python yaml_analyzer.py --rule4 --rule5')
    assert result == 256  # This will be the return code when rule4 and rule5 are set true at the same time
