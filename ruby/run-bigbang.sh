#!/bin/bash

echo -e '\n>>> Installing Ruby version manager...'
brew install rbenv

echo -e '\n>>> Installing Ruby...'
rbenv install 2.6.8
rbenv local 2.6.8

echo -e '\n>>> Installing Ruby tools...'
gem install bundler
gem install rake
rake install
