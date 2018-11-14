#!/bin/bash

if [ ! -e .gitignore ]; then
    echo "move to git repository"
    exit
fi

git rm --cached `git ls-files --full-name -i --exclude-from=.gitignore`