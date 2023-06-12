import requests
import json
import pandas as pd
import re

instance_url = "https://d5i00000e0otiea3-dev-ed.develop.my.salesforce.com"

url_for_token = f"{instance_url}/services/oauth2/token"

f = open('userinfo.json')
info = json.load(f)

payload = {
    'grant_type': info['grant_type'],
    'client_secret': info['client_secret'],
    'client_id': info['client_id'],
    'username': info['username'],
    'password': info['password']
    }


response = requests.request("POST", url_for_token, data=payload)

access_token = response.json()['access_token']



## add emailtemplate id hear
emailtemplateId = "00X5i0000032GYsEAM"


url_for_email = f"{instance_url}/services/data/v58.0/sobjects/EmailTemplate/{emailtemplateId}"

headers = {
  'Authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

response = requests.request("GET", url_for_email, headers=headers, data=payload)
#print(response.json())
email_body = response.json()['HtmlValue']

labels = re.findall("(?<=\{\!\$Label\.)(.*?)(?=\})",email_body)
labels = list(set(labels))
# print(len(labels))
df = pd.DataFrame(labels,columns = ['name'])

def get_labelid_by_name(name): 
    
    url_for_label = f"{instance_url}/services/data/v58.0/tooling/query?q=SELECT+Name,value+FROM+CustomLabel+where+name='{name}'"
    response = requests.request("GET", url_for_label,headers=headers)
    print(response.json())
    res = response.json()
    label_val = res['records'][0]['Value']

    return label_val


df['value'] = df['name'].apply(get_labelid_by_name)
print(df)
