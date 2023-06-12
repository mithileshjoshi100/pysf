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


