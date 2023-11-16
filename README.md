# How to reproduce
Tested with python 3.11

Install requirements:
`pip install -r requirements.txt`

Run tests with:
`python manage.py test tests`

# Expected result

Test outputs:

```
Base class method
Child class method
```

Running both base and child classes' `setUpTestData` methods.

# Actual result

Test outputs only `Base class method`

If @time_machine decorator is removed from the class, the test works as expected.