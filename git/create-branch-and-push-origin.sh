#!/bin/sh

BRANCH="$1"
START_POINT="$2"

git checkout -b $BRANCH $START_POINT
git push -u origin $BRANCH
