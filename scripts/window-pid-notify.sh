#!/bin/sh
PID=`xprop _NET_WM_PID | cut -d " " -f3`
echo $PID
notify-send $PID

