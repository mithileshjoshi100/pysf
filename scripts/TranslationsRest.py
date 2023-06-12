import requests
import json
import pandas as pd
from simple_salesforce import Salesforce 

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


url_for_label = f"{instance_url}/services/data/v58.0/tooling/sobjects/localizedvalue"

headers = {
  'Authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}
df = pd.read_csv('translations.csv')
df['isDeployed'] = False

def get_labelid_by_name(name): 
    
    url_for_label = f"{instance_url}/services/data/v58.0/tooling/query?q=SELECT+Name+FROM+CustomLabel+where+name='{name}'"
    response = requests.request("GET", url_for_label,headers=headers)
    print(response.json())
    res = response.json()
    label_id = res['records'][0]['attributes']['url'].split('/')[-1]

    return label_id

lang_keys = [ lang for lang in df.columns if lang != 'LabelName' and lang != 'isDeployed']

for index, row in df.iterrows():
    label_id = get_labelid_by_name(row['LabelName'])
    for lang in lang_keys:
        payload = json.dumps({
            "ParentId": label_id,
            "Language": lang,
            "Value": row[lang]
        })
            
        try:
            response = requests.request("POST", url_for_label, headers=headers, data=payload)
            is_deployed = response.json()['success']
        except:
            is_deployed = False

    df.at[index,'isDeployed'] = is_deployed


print("Completed Without Errors")