# conftest.py

import datetime
import pytest
import shutil

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.datetime.now()
    config.option.htmlpath = f"report/report-{now:%Y%m%d-%H%M%S}.html"
    # Copy content of current_version and new_version copy into current_version and new_version
    shutil.copyfile('current_version copy.yaml', 'current_version.yaml')
    shutil.copyfile('current_version copy.yaml', 'current_version.yaml')

