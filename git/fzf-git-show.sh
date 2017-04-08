#!/bin/sh

fzf_git_show() {
    fzf -0 --ansi --multi --preview-window=up \
        --preview="echo {} | sed -r ""'""s,^[|\\/* ]+([0-9a-zA-Z]|$),\1,""'"" | awk ""'""{print \$1}""' | xargs git show --color" \
    | sed -r 's,^[|\\/* ]+([0-9a-zA-Z]|$),\1,' \
    | awk '{print $1}'
}

if [ -t 0 ]; then
    # Terminal input (keyboard) - interactive
    git "$@" | fzf_git_show
else
    # input from pipe
    cat - | fzf_git_show
fi