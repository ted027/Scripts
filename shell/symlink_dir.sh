#!/bin/bash

read -p "source dir: " -c $pwd source_dir

if [ ! -e ${source_dir} ]; then
    echo "NOT EXIST"
fi

read -p "link dir: " -c $pwd/symlink link_dir

if [ ! -e ${link_dir} ]; then
    mkdir -p ${link_dir}
elif [ ! -d ${link_dir} ]; then
        echo "NOT DIRECTORY"
        exit
fi

read -p "all files? : " yn

for file in `find $source_dir -maxdepth 1 -type f`; do
    case "${yn}" in
        [yY]*) ;;
        *) read -p "crate symlink to ${file}? : " yn2
            case "${yn2}" in
                [yY]*) ;;
                *) echo "skipped." ; continue ;;
            esac ;;
    esac
    ln -s file link_dir/
done

read -p "Finished."