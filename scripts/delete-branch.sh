#!/bin/sh

BRANCH="$1"
if [ -z "$BRANCH" ]; then
    echo "Branch name must be given"
    exit 1
fi

set +x
mu branch -d "$BRANCH" && mu push --delete origin "$BRANCH" && remove-jenkins-view.py -n "$BRANCH"