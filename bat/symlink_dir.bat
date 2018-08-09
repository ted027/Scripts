@echo off

set source_dir=
set /P source_dir="source dir(double quotes): "
IF NOT EXIST "%source_dir%" (
    echo "NOT EXIST"
    exit
)

set link_dir=
set /P link_dir="link dir(double quotes): "

IF NOT EXIST "%link_dir%" (
    mkdir -p "%link_dir%"
) ELSE IF NOT EXIST "%link_dir%\" (
    echo "NOT DIRECTORY"
    exit
)

for %%i in (%source_dir%\*) do (
    echo "crate symlink to %%~nxi"
    mklink "%link_dir%\%%~nxi" "%source_dir%\%%~nxi"
)

pause