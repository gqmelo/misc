#!/bin/bash

export LIBGL_ALWAYS_INDIRECT=1
export DISPLAY=:1.0
for i in {0..9}; do
    python test_no_render.py $i
done
