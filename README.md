# Python-Salesforce
Python_Salesforce_Scripts

## Create Customlabels with RestAPI automation using Python Script

what you need
1. Authentication method
    salesforce org creds
        - username
        - password
        - clientid
        - clientsecrate
    or 
        -access token 
        (works for short time)

2. Python Scripts and Data files

### step 1
creat labels.csv like this


Name        |  Value
------------|-------------
Mance       |  Rayder     
Margaery    |  Tyrell     
Danerys     |  Targaryen  
Tyrion      |  Lannister  


### step 2

use `script/CustomLabelsRest.py`
add your creds and run file


## Create Customlabels Translations with RestAPI automation using Python Script

what you need
1. Authentication method
    salesforce org creds
        - username
        - password
        - clientid
        - clientsecrate
    or 
        -access token 
        (works for short time)

2. Python Scripts and Data files

### step 1
creat `translations.csv` like this


First Name  |  de         |  fr               
------------|-------------|----------------
Mance       |  deMance    |  frMance 
Margaery    |  deMargaery |  frMargaery        
Danerys     |  deDanerys  |  frDanerys           
Tyrion      |  deTyrion   |  frTyrion  


### step 2

use `script/TranslationsRest.py`
add your creds and run file