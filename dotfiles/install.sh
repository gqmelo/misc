#!/bin/bash

DOTFILES_DIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))

echo "Installing files from '$DOTFILES_DIR'"

ln -sf $DOTFILES_DIR/vimrc ~/.vimrc
ln -sf $DOTFILES_DIR/vscode-settings.json ~/.config/Code/User/settings.json
ln -sf $DOTFILES_DIR/vscode-keybindings.json ~/.config/Code/User/keybindings.json
