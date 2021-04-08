#!/bin/bash

# update
sudo apt update || sudo yum update

# Install Selenium webdriver and chrome
wget https://chromedriver.storage.googleapis.com/89.0.438.23/chromedriver_linux64.zip
unzip chromedriver_linux64.zip || sudo apt install unzip && unzip chromedriver_linux64.zip || sudo yum install unzip && unzip chromedriver_linux64.zip
sudo chmod +x chromedriver && sudo mv chromedriver /usr/bin/chromedriver

chromedriver --version

curl https://intoli.com/install-google-chrome.sh | bash || curl https://intoli.com/install-google-chrome.sh
sudo mv /usr/bin/google-chrome-stable /usr/bin/google-chrome

# install Python and dependencies
sudo apt install python3 || sudo yum install python3
pip3 --version || sudo apt install python3-pip || sudo yum install python3-pip
sudo pip3 install virtualenv || sudo apt install virtualenv || sudo yum install virtualenv

# Project-specific commands
mkdir dev
mkdir prod
mkdir prod/tkpy

# virtualenv --python=python3 venv
# source venv/bin/activate
# python3 -m pip install -r requirements.txt || echo "requirements.txt pip install failed, check to see file exists"

# python3 -m pip install async-timeout
# python3 -m pip install aiohttp
# python3 -m pip install selenium
# python3 -m pip install progress
# python3 -m pip install bs4
# python3 -m pip install --upgrade pandas
# python3 -m pip install --upgrade snowflake-sqlalchemy
# python3 -m pip install simple-salesforce
# python3 -m pip uninstall requests -y
# python3 -m pip install requests==2.22.0
# python3 -m pip install pybigquery
# python3 -m pip install numpy (needs verification)
# python3 -m pip install --upgrade snowflake-connector-python
# python3 -m pip install snowflake-connector-python[pandas]
# python3 -m pip install --upgrade parquet

google-chrome --version && which google-chrome
python --version && which python
