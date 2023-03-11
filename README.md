# YAML Analyzer
## Introduction
This is a YAML Analyzer tool that analyzes YAML files according to specific rules.

## Installation
1. Clone the repo from GitHub:
```bash
git clone https://github.com/your_username/your_repo.git
```
2. Navigate to the project directory:
```bash
cd your_repo
```
3. Create a virtual environment (optional but recommended):
```bash
python -m venv env
```
Activate the virtual environment:
```bash
source env/bin/activate # for Linux/MacOS
env\Scripts\activate.bat # for Windows
```
4. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
The main code is located in project/yaml_analyzer.py and can be run with the following command:

```bash
python project/yaml_analyzer.py [-h] [--rule4] [--rule5] [--log-level LOG_LEVEL] [--path-to PATH_TO]
```

Examples:
```bash
# Run with default rules with input files in current dir:
python yaml_analyzer.py

# Run with default rules, specifying location of input files:
python yaml_analyzer.py --path-to my/inputs

# Run applying optional rule 4
python yaml_analyzer.py --rule4

# Run applying optional rule 5
python yaml_analyzer.py --rule5

# Run with different logging levels
python yaml_analyzer.py --log-level info
```

Here are the available arguments:

-h: show help message and exit.
--rule4: enable rule 4 analysis.
--rule5: enable rule 5 analysis.
--log-level: set logging level (options: debug, info, warning, error, critical).
--path-to: specify path to YAML file for analysis.

## Running Tests
This project uses pytest to run the tests. To run the tests, simply run the following command in the project root directory:
```bash
# Run all tests
pytest

# Run specific scenario
pytest tests/scenarioN

# Run scenario, setting log level
pytest tests/scenarioN --log-level info
```
The test cases are located in project/tests. Each subdirectory represents a scenario, and each subdirectory contains three files: current_version, new_version, and expected_version.

## Reports
This project uses pytest-html to generate HTML reports. Reports are stored in the report folder with a unique name for each run. The name is in the format of report-{datetime}.html. The datetime is in the format of YYYYMMDD-HHMMSS.