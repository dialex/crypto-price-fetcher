#!/bin/bash
version='3.13.5'

echo -e '\n>>> Installing Python version manager...'
brew install pyenv
brew install pyenv-virtualenv

echo -e '\n>>> Installing Python...'
pyenv install $version
pyenv local $version
python -V
pip -V

echo -e '\n>>> Installing app dependencies...'
python -m pip install --upgrade pip
python -m pip install pipenv
pipenv --python $version
pipenv install
pipenv run pip list
