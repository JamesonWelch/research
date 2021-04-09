#!/bin/bash

# update
sudo yum update
# Install Selenium webdriver and chrome
wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip
unzip chromedriver_linux64.zip || sudo yum install unzip && unzip chromedriver_linux64.zip
sudo chmod +x chromedriver && sudo mv chromedriver /usr/bin/chromedriver
curl https://intoli.com/install-google-chrome.sh | bash || curl https://intoli.com/install-google-chrome.sh
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
# install Python and dependencies
sudo yum install python3
pip3 --version || sudo yum install python3-pip
sudo pip3 install virtualenv || sudo yum install virtualenv
# Project-specific commands
mkdir dev
mkdir prod
mkdir prod/tkpy
google-chrome --version && which google-chrome
python3 --version && which python3
chromedriver --version