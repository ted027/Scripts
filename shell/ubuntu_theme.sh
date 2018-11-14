#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y git build-essential

sudo add-apt-repository -y ppa:snwh/pulp
sudo apt update
sudo apt install paper-icon-theme -y
sudo apt install paper-gtk-theme -y
sudo apt install paper-cursor-theme -y

cd /tmp
sudo curl -sL https://github.com/nana-4/Flat-Plat/archive/v20180928.tar.gz | sudo tar xz
cd -
sudo /tmp/materia-theme-20180928/install.sh

sudo add-apt-repository ppa:papirus/papirus -y
sudo apt-get update
sudo apt-get install papirus-icon-theme -y