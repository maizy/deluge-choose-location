#!/bin/bash
PROJECT_DIR="/home/acer/Development/choose-location"
RES_EGG="${PROJECT_DIR}/chooselocation/dist/ChooseLocation-0.1-py2.6.egg"
cd "${PROJECT_DIR}/chooselocation"
find -type d -name '.AppleDouble' -exec rm -rf '{}' ';'
find -type f -name '.DS_Store' -exec rm -f '{}' ';'
rm "${RES_EGG}"
python setup.py bdist_egg
cp "${RES_EGG}" ~/.config/deluge/plugins/
sudo service deluge-daemon restart
