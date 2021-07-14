#!/bin/bash

sudo apt install python-is-python3
sudo apt install virtualenv -y
sudo apt install python3-venv

python -m venv venv
pip install -r ./requirements.txt

# As a service
# sudo cp ./mc_discord_bot.service /etc/systemd/system/
# sudo systemctl enable mc_discord_bot.service
# sudo systemctl start mc_discord_bot.service