#!/bin/bash
# script to set one monitor for wacom in linux
# xrandr --listmonitors TODO imporve getting monitor names
echo "Script for set wacom to cetain monitor"
xsetwacom --set "21" MapToOutput VGA-1-1
xsetwacom --set "20" MapToOutput VGA-1-1
