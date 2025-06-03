#!/bin/bash

DOTFILES_DIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))

echo "Installing files from '$DOTFILES_DIR'"

ln -sf $DOTFILES_DIR/bash/bashrc ~/.bashrc
ln -sf $DOTFILES_DIR/fish/config.fish ~/.config/fish/config.fish
ln -sf $DOTFILES_DIR/fish/functions ~/.config/fish/functions
