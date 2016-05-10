#!/bin/bash

export DISPLAY=:1.0

for i in {1..20}; do
    python test_glx_leak.py
    
    XEPHYR_RSS=`ps -up \`pidof Xephyr\` | tail -n1 | awk '{print $6}'`
    echo "Iteration $i, Xephyr RSS: $XEPHYR_RSS"
done
