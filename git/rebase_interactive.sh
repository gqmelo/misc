#!/bin/sh

if [ ! -z "$1" ]; then
    MERGE_BASE_BRANCH="$1"
else
    MERGE_BASE_BRANCH="master"
fi

echo "merge-base branch: $MERGE_BASE_BRANCH"
MERGE_BASE=`git merge-base $MERGE_BASE_BRANCH HEAD`
echo "Rebasing onto commit:"
echo $MERGE_BASE

git rebase -i $MERGE_BASE