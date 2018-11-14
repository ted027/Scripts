#!/bin/bash

read -p "which jdk? (8/9/10): " num

if [ ${num} -lt 8 -o ${num} -gt 10 ]; then
    echo "support only 8-10."
    exit

SITE=http://www.oracle.com
URL=$SITE$(curl -s $SITE/technetwork/java/javase/downloads/index.html | egrep -m1 -o "/technetwork/java/javase/downloads/jdk$num-downloads-[0-9]+\.html")
DOWNLOAD_URL=$(curl -s "$URL" | egrep -o "http://download\.oracle\.com/otn-pub/java/jdk/.*x64\.rpm")
wget -q --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" $DOWNLOAD_URL -O jdk${num}_x64.rpmz

read -p "install jdk? (y/N): " yn

case "$yn" in [yY]*) ;; *) exit ;; esac

rpm -ivh jdk${num}_x64.rpm
rm jdk${num}_x64.rpm