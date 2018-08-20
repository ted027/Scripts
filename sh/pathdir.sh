#!/bin/sh

if [ $1 = '-r' ]; then
    if [ `echo $PATH | grep $(pwd)` ]; then
        PATH = `echo $PATH | sed -e 's|$(pwd):||' | sed -e 's|:$(pwd)||'`
        export PATH
fi

if [ ! $# ]; then
    if [ ! `echo $PATH | grep $(pwd)` ]; then
        PATH=$(pwd):$PATH
        export PATH
fi
