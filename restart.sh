#!/bin/bash
RES_EGG="/home/acer/Development/choose-location/chooselocation/dist/ChooseLocation-0.1-py2.6.egg"
cd /home/acer/Development/choose-location/chooselocation
python setup.py bdist_egg
rm "${RES_EGG}"
cp /home/acer/Development/choose-location/chooselocation/dist/ChooseLocation-0.1-py2.6.egg ~/.config/deluge/plugins/
sudo service deluge-daemon restart
