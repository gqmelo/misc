#!/bin/sh

cat - | fzf --ansi --preview-window=up --preview='git show --color {1}'
