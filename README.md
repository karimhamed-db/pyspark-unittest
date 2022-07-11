# Pyspark Unit Testing Example 

This simple project was created to demonstrate how to start with unit testing your spark application in Python. When doing unit testing, it's important to understand that the tests will run locally and not on a separate cluster. Unit tests should run as fast as possible and run frequently to validate the logic of implemented code with any change.

When considering CI/CD, unit tests can run as part of the build and/or publish pipelines directly where if a test fail, the pipeline should be interupted and marked as failed.

This project uses [Pytest](https://docs.pytest.org/en/7.1.x/) as the testing framework and runner. But any other framework can work. 

## Project structure
When writing unit tests, it's important to separate the source code from the test code. The approach here is to have a separate `tests` directory that mimics the exact structure of the `src` directory.

```
project_path
├── src
│   └── module1
│         ├── script_1.py
│         ├── script_2.py
│         └── script_3.py
└── tests
    ├── data
    │     └── data_file1.csv
    └── test_module1
          ├── test_script_1.py
          ├── test_script_2.py
          └── test_script_3.py
```

## Running the tests

First install all dependencies required to run the tests.

```
pip install -r tests/requirements.txt
```

For running the tests, simply run

```
pytest
```

Pytest automatically discovers all available tests by loading all directories, files, classes and functions that `test` in their name. You can also explicitly pass in a directory if you want to run a specific set of tests.

```
pytest tests/test_spark_etl.py
```

## Extra

### Watcher
You can have your tests run automatically on any file change in the source code by using a watcher.

[pytest-watch](https://github.com/joeyespo/pytest-watch) is a package you can install to enable this feature.

```
pip install pytest-watch
```

Then just run this in a separate terminal session to have it continue running in the background.

```
ptw
```


### Coverage

You can also add coverage to your tests to see how much lines of codes your tests have ran. This is useful to detect section of codes that the tests may not have passed by or conditional branches that have not been executed.

[pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) is a package you can install to enable this feature.

```
pip install pytest-cov
```

Then to run to get a coverage output in the terminal. There are many other configuration with better formatted output (such as `HTML`)

```
pytest --cov=myproj --cov-report term
```