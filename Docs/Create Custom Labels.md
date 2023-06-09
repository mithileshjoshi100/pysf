# Create Custom Label in Buld
### let we have a csv file consist of two column and so many records the name on columns are LabelName and LabelValue
## Method 1
1. install sfdx cli tool provided by salesforce
2. create a new project and authrize a org using VS Code
3. create new file `CustomLabels.labels-meta.xml`
4. add all label details in the given format
```
<?xml version="1.0" encoding="UTF-8"?>
<CustomLabels xmlns="http://soap.sforce.com/2006/04/metadata">
    <labels>
        <fullName>Test1</fullName>
        <categories>test</categories>
        <language>en_US</language>
        <protected>true</protected>
        <shortDescription>Test1</shortDescription>
        <value>Test10</value>
    </labels>

    ... 
    ...
    ...


</CustomLabels>
```

5. click on CustomLabels.labels-meta.xml and select SFDX: Deplay this source to org
6. All the labels will be deployed to org


#### How to convert CSV file to xml 
use below python code
```

def create_xml_for_customlabels(filename):
    '''
    Change the verstions in xml if required
    input <= takes csv file name fist column: LabelName, second column: LabelValue
    output => NA
    this will create a xml file in same folder
    you can deploy this xml file using vs code
    '''

    df = pd.read_csv(filename)
    
    with open('labels.xml', "w") as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
        <CustomLabels xmlns="http://soap.sforce.com/2006/04/metadata">
        ''')
        for x,y in zip(df['LabelName'],df['LabelValue']):
            f.write(f'''
            <labels>
                <fullName>{x.strip()}</fullName>
                <categories>test</categories>
                <language>en_US</language>
                <protected>true</protected>
                <shortDescription>{x.strip()}</shortDescription>
                <value>{y.strip()}</value>
            </labels>
            ''')
        f.write('''
        </CustomLabels>''')
        
    print("XML Created")

```


you can also add categories, language paramenters in code


## Method 2

1. Manualy creat 1 coutom label, for refrence of program/ for example
2. run the below script 
    install python3 in system
    install simple_saleforce,pandas,requests modules
```
def create_labels_from_csv(file_name,sample_label_name):
    '''
    This function will take csv file name as input 
    file must contain 2 colums [name,value]
    input <= filename,labelname
    output => database operation
    '''

    df = pd.read_csv(file_name)

    try:
        sample_label = sf.mdapi.CustomLabel.read(sample_label_name)
    except:
        print("Please provide valid label name it is just for refrence of program")
        return 0
    
    for label,value in zip(df['name'],df['value']):
        print(label,value)
        sample_label.fullName = label
        sample_label.shortDescription = label
        sample_label.value = value
        sf.mdapi.CustomLabel.create(sample_label)
    
    return 1

create_labels_from_csv('csv_filename.csv',sample_label_name)
        
```
