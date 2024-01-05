# Playwright Pytests test

## Project Description

This project is a Python-based application that utilizes Playwright and Pytest for automated testing. The testing framework also integrates Allure for reporting purposes. The goal of this project is to provide a robust and efficient testing environment for web applications.

## Requirements

Make sure you have the following installed before running the tests:
```
pip install playwright pytest-playwright pytest allure-pytest Faker
```

## Steps to install
1. Clone the repository to your local machine:
```
git clone https://github.com/wasadar/playwright-pytest.git
```

2. Navigate to the project directory:
```
cd playwright-pytest
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Steps to run tests
Run the following command to execute the test suite:
```
pytest
```
This will initiate the Playwright tests using Pytest.

## Steps to Generate Report
After running the tests, generate an Allure report using the following command:
```
allure serve allure-results
```
This will open a local server and provide you with a link to view the generated report. Open the link in your browser to access detailed test results and insights.