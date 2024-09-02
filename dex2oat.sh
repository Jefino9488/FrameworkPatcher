#!/bin/bash

print() {
    echo -e "$@";
}

dex2oat() {
    file_dir="./oat/arm64/${file_n%.*}"
    mkdir -p ./oat/arm64
    rm -rf $file_dir.art $file_dir.odex $file_dir.vdex
    print "\nStarting compilation of file $file_n"
    ./dex2oat64 --dex-file=./$file_n --compiler-filter=everything --instruction-set=arm64 --dex-location=./$file_n --app-image-file=$file_dir.art --cpu-set=0,1,2,3,4,5,6,7 --oat-file=$file_dir.odex
    print "Compilation of file $file_n completed"
}

compile_all_files() {
    file=$(ls *.jar *.apk 2>/dev/null)

    if [ -z "$file" ]; then
        print "\nNo .jar or .apk files found in the directory.\n"
        exit 1
    fi

    for file_n in $file; do
        dex2oat
    done
}

# Main execution
compile_all_files
