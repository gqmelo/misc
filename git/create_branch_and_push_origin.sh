#!/bin/sh

BRANCH="$1"

git checkout -b $BRANCH
git push -u origin $BRANCH
