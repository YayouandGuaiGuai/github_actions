name: Pytest & flake8 control Push
on: push

jobs:
  qa:
    name: Check tests
    runs-on: ubuntu-20.04

    steps:
  - name: Checkout on master
    uses: actions/checkout@v3

  - name: Set up Python
    uses: actions/setup-python@master
    with:
      python-version: "3.x"

    - name: Install pytest and flake8
    run: |
         pip install pytest
         pip install flake8

    - name: Run tests
    run: |
        pytest

    - name: Run flake8
    uses: py-actions/flake8@v2