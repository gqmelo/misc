#!/bin/bash -x

gcc -g -mcmodel=large -c ml_main.c -o ml_mainreloc.o
gcc -shared -o libmlreloc.so ml_mainreloc.o
