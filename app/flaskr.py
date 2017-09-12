#!/usr/bin/env python
import http.client
import base64
import ssl
import sys
from flask import render_template, url_for
from flask import Flask, request, jsonify, session, redirect
import json

@app.route('/')
def index():
    return render_template('ise-wizard.html')


@app.route('/ise-wizard', methods=['GET, POST'])
def create_sgt():
    name = request.form['sgt-name']
    description = request.form['sgt-description']
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
      "Sgt" : {
        "id" : "-1",  
        "name" : name,
        "description" : description,
        "value": "-1"
      }
    }"""
    conn.request("POST", "/ers/config/sgt/", headers=headers, body=req_body_json)
    res = conn.getresponse()
    data = res.read()
    print("Status: {}".format(res.status))
    
