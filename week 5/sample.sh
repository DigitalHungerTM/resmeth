#!/bin/bash
# descr: this is a simple script that counts
#	 that counts the number of occurences
#	 of the word 'de' case insensitively
#
# usage: ./sample.sh file.txt

# test if a file is specified as the first argument
TEXT=$1
if [ -z "$TEXT" ]; then
	echo "Usage: ./sample.sh file.txt"
	exit
fi

# cat the file, find 'de', count
cat $1 |
grep -w -o -i 'de' |
wc -l
