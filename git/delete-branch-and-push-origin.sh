#!/bin/sh

BRANCH="$1"
if [ -z "$BRANCH" ]; then
    echo "Branch name must be given"
    exit 1
fi

set +x
git branch -d "$BRANCH" && mu push --delete origin "$BRANCH"
