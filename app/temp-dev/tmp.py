#!/usr/bin/env python
import http.client
import base64
import ssl
import sys
from flask import render_template, url_for
from flask import Flask, request, jsonify, session, redirect
import json
from decimal import Decimal
import yaml
import jinja2
from jinja2 import Environment, FileSystemLoader, Template

def createSGACL():
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
    req_body_json = """ {
      "Sgacl" : {
        "id" : "1235",
        "name" : "ZiaTest",
        "description" : "testing this",
        "ipVersion" : "IPV4",
        "aclcontent" : "Permit IP"
      }
    }"""

    req_body_json2 = """ { 
      "Sgacl" : {
        "id" : "1236",
        "name" : "tesst123",
        "description" : "testing sgacl creation",
        "ipVersion" : "IPV4",
        "aclcontent" : "Permit IP"
      }
    }"""

    print(req_body_json2)
    conn.request("POST", "/ers/config/sgacl/", headers=headers, body=req_body_json)
    res = conn.getresponse()
    data = res.read()
    print("Status: {}".format(res.status))
    return res.status

    
createSGACL();
