#!/bin/sh

if [ ! -z "$1" ]; then
    BRANCH="$1"
elif git rev-parse origin/mainline > /dev/null 2>&1; then
    BRANCH="origin/mainline"
else
    BRANCH="origin/master"
fi

git log \
    --abbrev-commit \
    --decorate \
    --date=relative \
    --format=format:'%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)' \
    $BRANCH..HEAD
