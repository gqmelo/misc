#!/bin/sh
PID=`xprop _NET_WM_PID | cut -d " " -f3`
echo $PID
echo $PID | xsel -i -b
cmdline=`cat /proc/$PID/cmdline | tr '\0' ' '`

notify-send "Process info" "PID: $PID
cmdline: $cmdline"

