#!/bin/sh

fzf_git_show() {
    filter="sed -r ""'""s,^[|\\/* ]+([0-9a-zA-Z]|$),\1,""'"" | cut -d ""'"" ""'"" -f1"
    fzf -0 --reverse --ansi --multi --preview-window=up \
        --preview="echo {} | $filter | xargs git show --color" \
        --bind "enter:execute(echo -n {+} | xargs copy-git-ref-to-clipboard)+accept" \
    | sed -r 's,^[|\\/* ]+([0-9a-zA-Z]|$),\1,' \
    | cut -d ' ' -f1 | tr '\n' ' '
}

if [ -t 0 ]; then
    # Terminal input (keyboard) - interactive
    git "$@" | fzf_git_show
else
    # input from pipe
    cat - | fzf_git_show
fi