#!/bin/bash
version='3.9.1'

echo -e '\n>>> Installing Python version manager...'
brew install pyenv

echo -e '\n>>> Installing Python...'
pyenv install $version
pyenv local $version
python3 -V
pip3 -V

echo -e '\n>>> Installing app dependencies...'
pip3 install pipenv
pipenv --python $version
pipenv install
pipenv run pip list
