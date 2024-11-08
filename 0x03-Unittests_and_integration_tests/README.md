# Unittest and Integration Tests
This project focuses on writing and understanding unit and integration tests in Python

## Learning Objectives
- Understand the difference between unit tests and integration tests.
- Apply common testing patterns such as mocking, parameterization, and fixtures.
- Use testing tools like unittest, unittest.mock and parameterized

## Requirements
+ Python version:3.7
+ OS: Ubuntu 18.04 LTS
+ Style guide: PEP8 and pycodestyle (v2.5)

## Project Files
+ utilis.py: Contains functions to be tested
+ client.py: Contains a class for accessing GitHub API data.
+ fixtures.py: Provides sample payloads for integration testing

## Running the Tests
Run all tests in the module:
```
python -m unittest discover
```
Or, run tests for a specific file:

```
python -m unittest path/to/test_file.py
```

## Key Concepts in Testing
1. **Unit Testing**: Tests individual functions or classes in isolation.
2. **Integration Testing**: Tests how various components work together in a larger context.
3. **Mocking:** Creates "fake" versions of objects or functions to control the behavior of dependencies during tests.
4. **Parameterization:** Allows running a single test with multiple inputs to validate various cases.

## Task List
Below is the task breakdown for this project:

1. **Parameterize a Unit Test:** Write a unit test for utils.access_nested_map.
2. **Parameterize Exception Tests:** Handle exceptions in utils.access_nested_map.
3. **Mock HTTP Calls:** Test the utils.get_json function by mocking HTTP responses.
4. **Memoization:** Test memoized properties to validate caching behavior.
5. **Mocking Properties:** Test a property in GithubOrgClient.
6. **Integration Test Setup:** Create integration tests for GithubOrgClient
