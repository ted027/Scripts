@echo off
cd /d %~dp0

set release_phase=
set /P release_phase="release phase[preST, ST, FC, RH]: "

set previous_version=
set /P previous_version="previous version: "
echo "previous version: %previous_version%"

set previous_date=
set /P previous_date="previous release date: "
echo "previous release date: %previous_date%"

set release_version=
set /P release_version="release version: "
echo "release version: %release_version%"

set this_release_date=
set /P this_release_date="this release date: "
echo "this release date: %this_release_date%"