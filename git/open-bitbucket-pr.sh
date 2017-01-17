#!/bin/bash

if [ ! -z "$1" ]; then
    MERGE_BASE_BRANCH="$1"
else
    MERGE_BASE_BRANCH="master"
fi

echo "merge-base branch: $MERGE_BASE_BRANCH"
MERGE_BASE=`git merge-base $MERGE_BASE_BRANCH HEAD`
HEAD=`git rev-parse HEAD`
CURRENT_BRANCH=`git rev-parse --abbrev-ref HEAD`
REPO_NAME=`basename $PWD`
if [ "$MERGE_BASE" = "$HEAD" ]; then
    echo "Skipping: HEAD and merge base are the same: $HEAD"
else
    PR_URL="https://eden.esss.com.br/stash/projects/ESSS/repos/$REPO_NAME/compare/commits?sourceBranch=refs/heads/$CURRENT_BRANCH"
    echo $PR_URL
    xdg-open "$PR_URL"
fi
