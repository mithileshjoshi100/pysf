'''
This is Simple Program to get the Instance of salesforce in python object
'''

from simple_salesforce import Salesforce


# Instantiate Salesforce object
sf = Salesforce(
    username='myemail@example.com', 
    password='password', 
    security_token='token'
    )

# sf = sf = Salesforce(
#     username=my_org_username,
#     password=my_org_password, 
#     consumer_key=client_id, 
#     consumer_secret=client_secret,
#     domain='test'
# )
