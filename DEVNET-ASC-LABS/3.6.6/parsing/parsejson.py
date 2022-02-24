# Fill in this file with the code from parsing JSON exercise
import json
import yaml


with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)

print (ourjson)

access_token = ourjson['access_token']
expire = ourjson['expires_in']
refresh_token = ourjson['refresh_token']
refreshtokenexpires_in = ourjson['refreshtokenexpires_in']

#print ("AccessToken", access_token)
#print ("ExpiresIn", expire)
#print ("RefreshToken Expire", refreshtokenexpires_in)


print ("----\n----")

print (yaml.dump(ourjson))

