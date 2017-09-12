#!/usr/bin/env python

###########################################################################
#                                                                         #
# This script demonstrates how to get the Guest users through ISE ERS     #
# API  by executing a Python script.                                      #
#                                                                         #
# SECURITY WARNING - DO NOT USE THIS SCRIPT IN PRODUCTION!                #
# The script allows connections to SSL sites without trusting             #
# the server certificates.                                                #
# For production, it is required to add certificate check.                #
#                                                                         #
# Usage: get-all-guest-users.py <ISE host><SponsorUser><SponsorPassword>  #
###########################################################################

import http.client
import base64
import ssl
import sys

# host and authentication credentials
host = sys.argv[1] # "10.200.99.97"
user = sys.argv[2] # "ersadmin"
password = sys.argv[3] # "Cisco1234"


conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))

creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

req_body_json = """ {
  "Sgt" : {
    "id" : "-1",    
    "name" : "test_zia_script",
    "description" : "This is a test",
    "value": "-1"
  }
}"""


conn.request("POST", "/ers/config/sgt/", headers=headers, body=req_body_json)

res = conn.getresponse()
data = res.read()

print("Status: {}".format(res.status))
print("Header:\n{}".format(res.headers))
print("Body:\n{}".format(data.decode("utf-8")))
