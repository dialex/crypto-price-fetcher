#!/bin/bash

echo -e '\n>>> Installing RVM...'
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB
curl -sSL https://get.rvm.io | bash

echo -e '\n>>> Installing Ruby...'
rvm install ruby
rvm --default use ruby

echo -e '\n>>> Installing Ruby tools...'
gem install bundler --no-rdoc --no-ri
gem install rake --no-rdoc --no-ri
