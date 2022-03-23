#!/bin/bash
# this is a program for finding tweets that contain the word 'haha'
# this is making use of the twitter2 corpus of the karora server.

# TODO: make more modular using tmpfiles
# TODO: make use of nested for loops to loop through files in folders in folders
# TODO: make use of the tweet2tab tool to extract the correct info

get_file_names () {
    ls /net/corpora/twitter2/Tweets/20*/* |
    grep '.out.gz' > $HOME/resmeth/filenames.txt
}


check_file () {
    # checking if the file exists, if it does; make it empty,
    # if it doesn't; make the file
    FILE=$HOME/resmeth/haha.txt
    if [ -f "$FILE" ]; then
        echo "" > $FILE
    else
        touch $FILE
    fi
}


zcat_files () {
    FILES=`cat $HOME/resmeth/filenames.txt`
    for file in $FILES
    do
        zcat $file |
        grep 'haha' >> $HOME/resmeth/haha.txt
    done
}


get_file_names
check_file
zcat_files
