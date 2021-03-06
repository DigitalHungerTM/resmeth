# Laughter vs Time of Day
This is the GitHub repo of all the code I wrote to help me with my research.  
The code can be copied and executed with
```commandline
$ ssh username@karora.let.rug.nl
$ git clone https://github.com/DigitalHungerTM/resmeth
$ cd resmeth
$ chmod +x counter.sh
$ ./counter.sh <day>/<month>
```
To recreate the data I have used run:
```commandline
$ ./counter.sh 16/<month> > data/data-16-<month>.txt
```
for every month in the range 01 - 12. The day and month should always be in double digits 
(e.g. 06/02 instead of 6/2). The ```data/filenames.txt``` file was generated by running:
```commandline
$ mkdir data
$ ls data/data*.txt > data/filenames.txt
```
After the script has finished, the collected data can be analyzed using 
```processor.py```. A python script that processes the data and displays it in a clear way. This script was used 
to generate graphs used in the paper. The python script requires the matplotlib package to be installed.
```commandline
$ pip install matplotlib
```
To run the python script:
```commandline
$ python3 processor.py data/filenames.txt pure|extended|plot
```
The output of the script will either be pure csv data, a pretty summary of the data, or a simple plot. The csv data is 
suitable to be saved as a .csv file by doing the following:
```commandline
$ python3 processor.py data/filenames.txt pure > data/pure.csv
```

### Important
- The counter.sh file should be edited in an advanced text editor like vscode because other simple editors might
not be able to interpret the emojis used in the regular expression to detect laughter.  
- The ```counter.sh``` script should be executed from within the karora servers as it will try to use the 
```/net/corpora/twitter2``` corpus and tools to collect the data.
- The ```processor.py```'s plotting function only works in an environment with a graphical interface.
