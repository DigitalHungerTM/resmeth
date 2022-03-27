#!/bin/bash
# a counter that counts tweets that contain signs of laughter

#constants:
TWEETS="/net/corpora/twitter2/Tweets"
date=$1
emojis="[😂]"

check_arg () {
    if [ -z "$date" ]; then
        echo
        echo "usage: ./counter.sh date"
        echo "format of the date: hour/day/month/year"
        echo "example: 01/09/11/2011"
        echo "allowed dates: 19/16/12/2010 - 23/31/03/2022"
        echo
        exit
    fi
}


# format: hour/day/month/year
# date="01/30/06/2011"
format () {
    hour=`echo $date| cut -d '/' -f1`
    day=`echo $date | cut -d '/' -f2`
    month=`echo $date | cut -d '/' -f3`
    year=`echo $date | cut -d '/' -f4`
    path="$TWEETS/$year/$month/$year$month$day:$hour.out.gz"
}


count_happy () {
    number=`gunzip -c "$path" |
    /net/corpora/twitter2/tools/tweet2tab -i text date|
    grep -e "haha" -e "HAHA" -e "XD" -e "xd" -e "lol" -e "LOL" -e ":)" -e "(:" -e "😂" -e "🤣" |
    cut -d ' ' -f1 |
    grep -v "RT" |
    wc -l`
    echo "number of tweets that express laughter: $number"
}


count_total () {
    number=`gunzip -c "$path" |
    wc -l`

    echo "total number of tweets: $number"
}


format
check_arg
count_total
count_happy
