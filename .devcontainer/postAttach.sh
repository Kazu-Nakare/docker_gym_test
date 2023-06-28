#!/bin/bash

# export DISPLAY=:0
Xvfb :0 -screen 0 1400x900x24 &
x11vnc -display :0 -forever -noxdamage > /dev/null 2>&1 &
icewm-session &
