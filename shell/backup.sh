#!bin/sh

input="/Volumes/*iphone_name*/*画像フォルダ名*"
output="/Volumes/*hdd_name*/*フォルダ名*"

for file in `find input -maxdepth 1 -type f`; do
    YYYYMM=`date +%Y%m -r $file`
    MMDD=`date +%m%d -r $file`
    # 保存先ディレクトリがなければ作る
    target_dir="${output}/${YYYYMM}/${MMDD}"
    if [ ! -d target_dir ]; then
        mkdir -p target_dir
    fi
    cp -i $file $output$YYYYMM$MMDD
done