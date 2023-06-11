import requests
import json
import pandas as pd

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



url_for_label = f"{instance_url}/services/data/v58.0/tooling/sobjects/ExternalString"

headers = {
  'Authorization': f'Bearer {access_token}',
  'Content-Type': 'application/json'
}

df = pd.read_csv('data.csv')
df['isDeployed'] = False
try:
    for index, row in df.iterrows():
        payload = json.dumps({
            "Name": row['Name'].strip(),
            "MasterLabel": row['Name'].strip(),
            "Value": row['Value'].strip(),
            "IsProtected": True,
            "language": "en_US",
            "Category": "test"
        })
        
        try:
            response = requests.request("POST", url_for_label, headers=headers, data=payload)
            is_deployed = response.json()['success']
        except:
            is_deployed = False

        df.at[index,'isDeployed'] = is_deployed
except:
    print('Somethig Went Wrong')

finally:
    df.to_csv('Result.csv')
