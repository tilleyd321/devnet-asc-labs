curl -k -X POST -F 'username=rick'  -F 'password=samepassword'  'https://0.0.0.0:5000/signup/v2'
curl -k -X POST -F 'username=allan' -F 'password=samepassword'  'https://0.0.0.0:5000/signup/v2'
curl -k -X POST -F 'username=dave'  -F 'password=differentpwd'  'https://0.0.0.0:5000/signup/v2'
