#!/bin/bash

echo -e '\n>>> Installing Python...'
brew install python3
python -V
pip -V

echo -e '\n>>> Installing Python version manager...'
brew install pyenv
pyenv install 3.8.2
pyenv global 3.8.2

echo -e '\n>>> Installing Python tools...'
brew install pipenv
pipenv install
pipenv run pip list
