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
echo "Checking out commit:"
echo $MERGE_BASE

git checkout $MERGE_BASE