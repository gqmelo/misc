#!/bin/bash -x

gcc -c c_rc.c
gcc -o c_rc -static -Wl,-verbose c_rc.o
