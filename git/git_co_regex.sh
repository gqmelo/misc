#!/bin/bash

if [ $# -gt 1 ]; then
    git checkout $*
    exit
fi

set -e
all_branches=$(git for-each-ref --format='%(refname:short)' refs/heads/)
branch_name=$(echo $all_branches | tr ' ' '\n' | grep "$1")
number_of_branches=$(echo $branch_name | tr ' ' '\n' | wc -l)
if [[ $number_of_branches -eq 1 ]]; then
    git checkout $branch_name
else
    git checkout $*
fi
