#!/bin/sh

g++ -g -O2 -shared -fPIC -o libdummy_llvm.so dummy_llvm.cpp -static-libstdc++ -Wl,--version-script=dummy_llvm.map
#g++ -g -O2 -shared -fPIC -o libdummy_llvm.so dummy_llvm.cpp -static-libstdc++
g++ -g -O2 -o string_crash string_crash.cpp -ldummy_llvm -L. -Wl,-rpath='$ORIGIN'
