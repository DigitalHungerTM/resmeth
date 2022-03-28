#!/bin/bash
# a counter that counts tweets that contain signs of laughter

#constants:
TWEETS="/net/corpora/twitter2/Tweets"
HOURS="00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23"
YEARS="2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021"

arg=$1
arg_check () {
    if [ -z "$arg" ]; then
        echo
        echo "Error: expected an argument"
        echo "Usage: ./counter.sh Day/Month"
        echo "Example: ./counter.sh 06/11"
        echo
        exit
    fi
}

# format: hour/day/month/year
# formats the date to be used as a filename
format () {
    date=$1
    hour=`echo $date| cut -d '/' -f1`
    day=`echo $date | cut -d '/' -f2`
    month=`echo $date | cut -d '/' -f3`
    year=`echo $date | cut -d '/' -f4`
    path="$TWEETS/$year/$month/$year$month$day:$hour.out.gz"
}


# counts the number of tweets in a file that contain some form of laughter
count_happy () {
    number=`gunzip -c "$path" |
    /net/corpora/twitter2/tools/tweet2tab -i text date|
    grep -e "haha" -e "HAHA" -e "Haha" -e "XD" -e "xd" -e "Xd" -e "lol" -e "LOL" -e "Lol" -e "lmao" -e "Lmao" -e "LMAO" -e "hehe" -e "Hehe" -e "HEHE" -e "😂" -e "🤣" -e "😹" |
    cut -d ' ' -f1 |
    grep -v "RT" |
    wc -l`
    echo "$number : tweets that express laughter"
}


# counts the total number of tweets in a file
count_total () {
    number=`gunzip -c "$path" |
    wc -l`
    echo "$number : total tweets"
}


# generates the needed dates and passes them to the format function to be processed further
# and generates the output using count_happy and count_total
main () {
    arg_check
    dayMonth=$1

    for hour in $HOURS; do
        for year in $YEARS; do
            date="$hour/$dayMonth/$year"
            echo $date
            format "$date"
            count_happy
            count_total
            echo
        done
    done
}


# execute the main function
main $1





