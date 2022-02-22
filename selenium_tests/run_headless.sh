#!/bin/bash


echo -e "Start xvfb"
exec -a xvfb Xvfb :1 -screen 0 1024x768x16 &> xvfb.log  &

DISPLAY=:1.0
export DISPLAY

echo -e "Run tests"

PATH="./:$PATH" python3.7 main.py https://etu.ru


rcode=$?
echo -e "Stop xvfb"
kill $(pgrep -f xvfb)
exit ${rcode}
