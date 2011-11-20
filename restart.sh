#!/bin/bash

SCRIPT_PATH=$(cd ${0%/*} && echo $PWD/${0##*/})
PROJECT_DIR=`dirname "$SCRIPT_PATH"`
RES_EGG="${PROJECT_DIR}/chooselocation/dist/ChooseLocation-0.1-py2.6.egg"
PLUGINS_DIR="~/.config/deluge/plugins/"

cd "${PROJECT_DIR}/chooselocation"

find -type d -name '.AppleDouble' -exec rm -rf '{}' ';'
find -type f -name '.DS_Store' -exec rm -f '{}' ';'

rm "${RES_EGG}"
python setup.py bdist_egg
echo "RESULT EGG: ${RES_EGG}"
cp "${RES_EGG}" "${PLUGINS_DIR}"

sudo service deluge-daemon restart
