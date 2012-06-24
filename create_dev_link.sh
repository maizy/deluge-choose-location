#!/bin/bash
cd /home/acer/Development/choose-location/chooselocation
mkdir temp
export PYTHONPATH=./temp
python setup.py build develop --install-dir ./temp
cp ./temp/ChooseLocation.egg-link /home/acer/.config/deluge/plugins
rm -fr ./temp
