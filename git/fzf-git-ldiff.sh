#!/bin/sh

fzf_git_ldiff() {
    fzf -0 --reverse --ansi --multi --preview-window=up \
        --preview="echo {} | sed -r ""'""s,^[|\\/* ]+([0-9a-zA-Z]|$),\1,""'"" | awk ""'""{print \$1}""' | xargs git ldiff" \
    | sed -r 's,^[|\\/* ]+([0-9a-zA-Z]|$),\1,' \
    | awk '{print $1}'
}

if [ -t 0 ]; then
    # Terminal input (keyboard) - interactive
    git "$@" | fzf_git_ldiff
else
    # input from pipe
    cat - | fzf_git_ldiff
fi