from Connect import sf 
import re
import pandas as pd


def get_label_by_name(name):
    '''
    input <= name of customlabel 
    output => value of customlabel
    '''
    label_v = None
    try:
        label_v = sf.mdapi.CustomLabel.read(name).value
    except:
        label_v = f'{name} Not a label'
    return label_v


def get_all_labels_from_email(templateId):
    '''
    This is a experimental function
    this fuction well search `{!Label.*}` this patern 
    will also include labels from comments
    will not include labels from component if used 

    input <= email template id from salesforce
    output => datafrem consist of CustomLabel name and its value
    '''
    try:
        email_body = sf.EmailTemplate.get(templateId)
    except:
        print('Email Not Found')
        return None
    
    labels = re.findall("(?<=\{\!\$Label\.)(.*?)(?=\})",email_body['Markup'])
    df = pd.DataFrame(labels,columns = ['name'])

    df['value'] = df['name'].apply(get_label_by_name)

    # you can add your logic hear and 
    # use this for silection based on requirement

    #df.to_csv(f'{templateId}_labels.csv')

    return df


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



def create_xml_for_tranlations(filename,p1,p2):
    '''
    Change the verstions in xml if required
    input <= takes csv file name, colum name for label, colum name for transaltion
    output => NA
    this will create a xml file in same folder
    you can deploy this xml file using vs code
    '''

    df = pd.read_csv(filename)
    
    with open('translations.xml', "w") as f:
        f.write('''<?xml version="1.0" encoding="UTF-8"?>
        <Translations xmlns="http://soap.sforce.com/2006/04/metadata">
        ''')
        for x,y in zip(df[p2],df[p1]):
            f.write(f'''
            <customLabels>
                <label>{x.strip()}</label>
                <name>{y.strip()}</name>
            </customLabels>
            ''')
        f.write('''
        </Translations>''')
        
    print("XML Created")


def delet_labels_from_csv(filename):
    '''
    input <= pass a csv file name must contain a single column with name CustomLabel
    output => will delet customlabels from database
    '''
    df = pd.read_csv(filename)
    full_names = []
    for label_name in df['CustomLabel']:
        if len(full_names) == 10:
            sf.mdapi.CustomLabel.delete(full_names)
            full_names = []
        full_names.append(label_name)
    sf.mdapi.CustomLabel.delete(full_names)

    







