# Ebay-Data
CS40 data scrapping project


Hello! I created this repository for my data scrapping project for my cs40 class. you can find instructions to the project [here](https://github.com/mikeizbicki/cmc-csci040/tree/2022fall/project_03)


If you clicked on the link you know that this file explains how the whole thing works. And if you did not click on the link or did not bother to read all the way down... well now you know. 


So let me outline what ebay_dl.py does: 


My file first defines couple of arguments, one to define the term you want to look up, another to indicate how many pages of information you want to extract, and another to convert the information into a csv file rather than a json. 

For this project, ebay_dl.py extracts the name 

to extract the other files on this repository I used the following commands:

```
 /Users/pedroarellano/Documents/GitHub/Ebay-Data/ebay_project/ebay_dl.py garmin --num_pages=10
```
or 

```
 /Users/pedroarellano/Documents/GitHub/Ebay-Data/ebay_project/ebay_dl.py 'flying octopus' --num_pages=10
```
and to obtain the csv I simply added the last command

```
 /Users/pedroarellano/Documents/GitHub/Ebay-Data/ebay_project/ebay_dl.py 'flying octopus' --num_pages=10 --csv=True 
```
Thank you 
ok bye! 