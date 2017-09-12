#!/usr/bin/env python

import http.client
import base64
import ssl
import sys
import json
from decimal import Decimal
import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader, Template

# host and authentication credentials
host = "10.200.99.97"
user = "ersadmin"
password = "Cisco1234"

conn = http.client.HTTPSConnection("{}:9060".format(host), context=ssl.SSLContext(ssl.PROTOCOL_TLSv1_2))
creds = str.encode(':'.join((user, password)))
encodedAuth = bytes.decode(base64.b64encode(creds))

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'authorization': " ".join(("Basic",encodedAuth)),
    'cache-control': "no-cache",
    }

env = Environment(loader=FileSystemLoader('./'))
baller = "Zia Syed"
ballerd = "Baller"

jd = {}
jd["id"] = "-1"
jd["name"] = baller
jd["description"] = ballerd
jd["value"] = "-1"
for k, v in jd.items():
    print(k, v)

jds = json.dumps(jd)
print(json.dumps(jd, ensure_ascii=False))

file_handle = open("temp.yml")
m = yaml.safe_load(file_handle)
file_handle.close()
m = json.dumps(m)
print(m)

req_body_json = """{
  "Sgt" : {
    "id" : -1,    
    "name":"zbasller1",
    "description":"hello",
    "value": -1
  }
}"""

ho = {}
ho["sgtName"] = "zaza"
ho["sgtDescription"] = 1

template = env.get_template("tmp.j2")
file_name = "letsgo"
with open('letsgo', 'w') as config_file:
    config_file.write(template.render(config=ho))
    config_file.close()


env = Environment(loader=FileSystemLoader('./'))
template = env.get_template("hell.j2")
with open('rendered.txt', 'w') as config_file:
    config_file.write(template.render(id='-1', name=baller, description=ballerd, value='-1'))
    config_file.close()


print(req_body_json)
with open('rendered.txt', 'r') as fin:
    print(fin.read())
 
conn.request("POST", "/ers/config/sgt/", body=req_body_json, headers=headers)

res = conn.getresponse()
data = res.read()

print("Status: {}".format(res.status))

