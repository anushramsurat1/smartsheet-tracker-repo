import http.client
import base64
import ssl
import sys
import json
from flask import render_template, url_for
from flask import Flask, request, jsonify, session, redirect

# host and authentication credentials
host = sys.argv[1] # "10.200.99.97"
user = sys.argv[2] # "ersadmin"
password = sys.argv[3] # "Cisco1234"


conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

headers = {
    'accept': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

conn.request("GET", "/ers/config/sgt/", headers=headers)

res = conn.getresponse()
data1 = res.read()

#data2 = json.loads(data1.get_data(as_text=True))
data3 = json.loads(data1.decode('utf-8'))

for k, v in data3.items():
    print("we have", k, v)

#print(data2)
#print(data3)


print("Body:\n{}".format(data1.decode("utf-8")))
