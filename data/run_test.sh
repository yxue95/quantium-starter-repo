#!/bin/bash

# activate virtual environment
source venv/bin/activate

# run test suite
python -m pytest test_app.py

# capture exit code
exit_code=$?

# deactivate virtual environment
deactivate

# exit with captured exit code
exit $exit_code
