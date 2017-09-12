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

# The below JSON payload applies SGACL 'az' ("06fd32e0-6cca-11e7-a50d-005056b41003")
# Between the source sgt apple_lowsec_user (82fdc340-6023-11e7-a50d-005056b41003) and
# and the destinarion sgt apple_db_servers (2eb7ca30-6026-11e7-a50d-005056b41003).
# The default reule is NONE (no action) and Cell Status is marked as ENABLED.
req_body_json = """ {
  "EgressMatrixCell" : {
    "sourceSgtId" : "0bbc0c20-6f8b-11e7-a50d-005056b41003",
    "destinationSgtId" : "9a449560-6f8c-11e7-a50d-005056b41003",
    "matrixCellStatus" : "ENABLED",
    "defaultRule" : "NONE",
    "sgacls" : [ "0a02b170-6f8d-11e7-a50d-005056b41003" ]
  }
}"""



# Note below CELL create call succeeds only once.
# If the CELL needs to be recreated, it must first be deleted in ISE
conn.request("POST", "/ers/config/egressmatrixcell/", headers=headers, body=req_body_json)

res = conn.getresponse()
data = res.read()

print("Status: {}".format(res.status))
print("Header:\n{}".format(res.headers))
print("Body:\n{}".format(data.decode("utf-8")))
