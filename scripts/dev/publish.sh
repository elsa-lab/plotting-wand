#!/bin/bash
#
# Package and distribute the project to PyPI
#
# Reference: https://packaging.python.org/guides/distributing-packages-using-setuptools/

# Handle errors
source scripts/dev/includes/error_handling.sh

# Print the goal of this script
echo "Publish the project to PyPI"

# Install required pakcages
pip install twine
pip install wheel

# Create a source distribution
python setup.py sdist

# Build the wheel and capture the outputs
WHEEL_OUTPUTS=$(python setup.py bdist_wheel)

# Print the wheel outputs
echo "$WHEEL_OUTPUTS"

# Upload the distributions
twine upload dist/*

# Print success message
echo "Successfully published the project to PyPI"
