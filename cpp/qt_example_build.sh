#!/bin/bash -x

g++ -o qt_example qt_example.cpp -I$CONDA_PREFIX/include -I$CONDA_PREFIX/include/qt -L $CONDA_PREFIX/lib -lQt5Widgets -lQt5Gui -lQt5Core -licui18n -licudata -licuuc
