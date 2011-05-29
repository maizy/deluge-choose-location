#!/bin/bash
cd /home/acer/Development/choose-location/chooselocation
python setup.py bdist_egg
./create_dev_link.sh
sudo service deluge-daemon restart
