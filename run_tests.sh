#!/bin/bash

# 1. Activate the virtual environment
# We check the common location for the venv activation script
source venv/Scripts/activate

# 2. Execute the test suite
# We run pytest directly
pytest

# 3. Handle the exit code
# $? captures the exit status of the last command (pytest)
TEST_EXIT_CODE=$?

if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0
else
    echo "Tests failed with exit code $TEST_EXIT_CODE"
    exit 1
fi