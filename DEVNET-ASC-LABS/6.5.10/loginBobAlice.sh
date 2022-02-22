#!/bin/bash
curl -k -X POST -F 'username=bob'   -F 'password=passwordforbob'  'https://0.0.0.0:5000/login/v1'
curl -k -X POST -F 'username=alice' -F 'password=myalicepassword' 'https://0.0.0.0:5000/login/v1'

