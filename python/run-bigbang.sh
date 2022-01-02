#!/bin/bash
version='3.9.6'

echo -e '\n>>> Installing Python version manager...'
brew install pyenv
brew install pyenv-virtualenv

echo -e '\n>>> Installing Python...'
pyenv install $version
pyenv local $version
python3 -V
pip3 -V

echo -e '\n>>> Installing app dependencies...'
sudo -H pip3 install -U pipenv
pipenv --python $version
pipenv install
pipenv run pip list
