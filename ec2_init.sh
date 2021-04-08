#!/bin/bash

# update
sudo apt update

# install Python and dependencies
sudo apt install python3
sudo pip3 install selenium || sudo apt install python3-pip
sudo pip3 install virtualenv || sudo apt install virtualenv

# Project-specific commands
mkdir dev
mkdir prod
cd prod

virtualenv --python=python3 venv
source venv/bin/activate
python3 -m pip install -r requirements.txt || echo "requirements.txt pip install failed, check to see file exists"

# Install Selenium webdriver and chrome
wget https://chromedriver.storage.googleapis.com/89.0.438.23/chromedriver_linux64.zip
unzip chromedriver_linux64.zip || sudo apt install unzip && unzip chromedriver_linux64.zip
sudo chmod +x chromedriver && sudo mv chromedriver /usr/bin/chromedriver

chromedriver --version

curl https://intoli.com/install-google-chrome.sh | bash || curl https://intoli.com/install-google-chrome.sh
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome
google-chrome --version && which google-chrome