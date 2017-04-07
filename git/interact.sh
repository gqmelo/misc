#!/bin/sh

fzf_git_show() {
    fzf -0 --ansi --preview-window=up --preview='git show --color {1}'
}

if [ -t 0 ]; then
    # Terminal input (keyboard) - interactive
    git "$@" | fzf_git_show
else
    # input from pipe
    cat - | fzf_git_show
fi