#!/bin/bash
version='3.10.2'

echo -e '\n>>> Installing Python version manager...'
brew install pyenv
brew install pyenv-virtualenv

echo -e '\n>>> Installing Python...'
pyenv install $version
pyenv local $version
python3 -V
pip3 -V

echo -e '\n>>> Installing app dependencies...'
python3 -m pip install --upgrade pip
python3 -m pip install pipenv
pipenv --python $version
pipenv install
pipenv run pip list
