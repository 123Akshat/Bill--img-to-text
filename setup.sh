#!/bin/bash

# Create a Python virtual environment
python3 -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install the required packages
pip install -r requirements.txt

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt-get update
    sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn

elif [[ "$OSTYPE" == "darwin"* ]]; then
    brew install tesseract
fi

# Deactivate the virtual environment
deactivate
