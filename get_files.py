import json
import os
import requests
import requests.auth
from datetime import datetime

auth_dict = {}
with open("auth.json", "r") as auth_file:
    auth_dict = json.load(auth_file)

clientID = auth_dict['clientID']
secretKey = auth_dict['secretKey']
reddit_username = auth_dict['reddit_username']
reddit_password = auth_dict['reddit_password']

now = datetime.now()
data_download_dir = "data_download/"+now.strftime("%Y-%m-%d-%H-%M")

if not os.path.exists(data_download_dir):
    os.makedirs(data_download_dir)

print("Getting access token...")

client_auth = requests.auth.HTTPBasicAuth(clientID, secretKey)
post_data = {"grant_type": "password", "username": reddit_username, "password": reddit_password}
headers = {"User-Agent": "saved-script/0.1 by /u/devprabal"}
response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

print("Getting files...")

access_token = response.json().get('access_token')
authorization_str = "bearer "+access_token
headers = {"Authorization": authorization_str, "User-Agent": "saved-script/0.1 by /u/devprabal"}
endpoint = "https://oauth.reddit.com/user/"+reddit_username+"/saved?limit=100"
response = requests.get(endpoint, headers=headers)

response_dict = response.json()

count = 1
filename = data_download_dir+"/"+"saved-msg-"+str(count)+".json"
with open(filename, "w") as write_file:
    json.dump(response_dict, write_file)
count = count + 1

print("Saved file..."+filename)

after = response_dict['data']['after']

while after != None:
    endpoint = "https://oauth.reddit.com/user/"+reddit_username+"/saved?limit=100&after="+after
    response = requests.get(endpoint, headers=headers)

    response_dict = response.json()
    after = response_dict['data']['after']

    filename = data_download_dir+"/"+"saved-msg-"+str(count)+".json"
    with open(filename, "w") as write_file:
        json.dump(response_dict, write_file)
    count = count + 1
    
    print("Saved file..."+filename)
print("Done.\nRun trim_data.py script now.")
