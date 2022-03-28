# Research Methods Final Project
This is the Github repo of all the code I wrote to help me with my research.  
The code can be copied and executed with
```commandline
$ ssh username@karora.let.rug.nl
$ git clone https://github.com/DigitalHungerTM/resmeth
$ cd resmeth
$ chmod +x counter.sh
$ ./counter.sh
```

This code should be executed from within the karora servers as it will try to use the ```/net/corpora/twitter2``` 
corpus and tools to collect the data. By editing the value of ```dayMonth``` in the main function of ```counter.sh``` 
you can change the date that the script will analyze. The day and month should always be in double digits 
(e.g. 06/02 instead of 6/2). Note that the code should be edited in VScode or Pycharm as 
other text editors might not be able to interpret the emojis correctly. After the script has finished, the collected 
code can be analyzed using the ```python script```