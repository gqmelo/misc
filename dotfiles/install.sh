#!/bin/bash

DOTFILES_DIR=$(dirname ${BASH_SOURCE[0]})

echo "Installing files from '$DOTFILES_DIR'"

ln -sf $DOTFILES_DIR/vimrc ~/.vimrc
