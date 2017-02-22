#!/bin/bash -x

nasm -f elf64 nasm_rc.asm -o nasm_rc.o
ld -o nasm_rc64 nasm_rc.o
