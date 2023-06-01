# **Automation Testing UI: Online Shop**

# Project Overview

This is a project for a test online shop that simulates basic functionalities 
commonly found in such websites. 

The project utilizes Python, Pytest, and Selenium for automated smoke testing. 
The tests are designed to verify the functionality and user experience of the online shop. 
The test results are recorded and presented in an Allure report, providing comprehensive 
information about test execution.
The tests involve checking the functionality of the website in the Google Chrome browser.

### Test Coverage

The automated tests cover the following scenarios:

1. Authorization and Access to the Product Catalog
2. Product Sorting
3. Adding Two Products to Cart and Checking Cart Contents
4. Confirmation and Completion of the Order

For detailed information, please refer to the [Checklist for Automation Testing UI: Online Shop](./checklist.md).

### Allure Report

The test results are presented in an Allure report, which provides a clear and 
structured overview of the test execution. The report includes information such as test status,
duration, and attached screenshots. Screenshots are stored in the project directory and are accessible
through the Allure report.

## Getting Started

To set up the project and run the tests, please follow these steps:

- Clone the project repository to your local machine.
- Install the required dependencies using pip (commands 'pip install pytest', 'pip install selenium').
- Execute the tests using the provided Pytest command 'python -m pytest --alluredir=test_results/ tests/test_order_online_shop.py'.
- View the generated Allure report to analyze the test results.

To see an example of the Allure report, refer to the [allure_report.png](./test_results/allure_report.png) file.

## Requirements

Make sure you have the following installed:

- Python 3.x
- Pytest
- Selenium
- Allure Command Line Interface (CLI)

Note: The tests were carried out using the Google Chrome browser (version 113.0.5672.127).

## Contact

If you have any questions or inquiries regarding this project, 
please feel free to contact me at [liliya_s@ukr.net](liliya_s@ukr.net).