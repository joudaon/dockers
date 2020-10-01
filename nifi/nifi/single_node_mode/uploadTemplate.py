import os
import json
import requests

"""
Upload Nifi templates to Nifi root Process Group of an unsecured Nifi instance.
REST API is used. 
More info: https://nifi.apache.org/docs/nifi-docs/rest-api/index.html
"""

# https://stackoverflow.com/questions/38446620/post-a-nifi-template-via-rest

url = 'http://localhost:8080'
templatesPath = '/mypath'

r = requests.get(url + '/nifi-api/flow/process-groups/root').json()

proccessGroup = r['processGroupFlow']['id']

print(proccessGroup)

for file in os.listdir(templatesPath):
  filepath = os.path.join(templatesPath, file)
  r=requests.post("{}/nifi-api/process-groups/{}/templates/upload".format(url,proccessGroup), files={"template": open( filepath, 'rb')} )
  if (r.status_code == 201):
    print(file + "template successfully uploaded.")
  else:
    print("Error.")
