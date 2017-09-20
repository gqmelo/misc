#!/bin/sh

if [ ! -z "$1" ]; then
    MERGE_BASE_BRANCH="$1"
elif git rev-parse mainline; then
    MERGE_BASE_BRANCH="mainline"
else
    MERGE_BASE_BRANCH="master"
fi

echo "merge-base branch: $MERGE_BASE_BRANCH"
MERGE_BASE=`git merge-base $MERGE_BASE_BRANCH HEAD`
HEAD=`git rev-parse HEAD`
if [ "$MERGE_BASE" = "$HEAD" ]; then
    echo "Skipping rebase, HEAD and merge base are the same: $HEAD"
elif [ "`git rev-list $MERGE_BASE..HEAD`" = "$HEAD" ]; then
    echo "Skipping rebase, HEAD contains only one commit"
else
    echo "Rebasing onto commit:"
    echo $MERGE_BASE
    git rebase -i $MERGE_BASE
fi
