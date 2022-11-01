#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify

app = Flask(__name__)

def parse_data(args):
    r = {}
    for k,v in args.items():
        r[k] = v
    return r

def parse_request_data():
    res = {
        'args': parse_data(request.args),
        'headers': parse_data(request.headers),
        'origin': request.remote_addr,
        'url': request.base_url
    }
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        res['form'] = parse_data(request.form)
        res['json'] = parse_data(request.json)
    return res

@app.route("/sample/hello", methods=['GET', 'POST'])
def hello_world():
    return jsonify(parse_request_data())

@app.route("/sample/callback", methods=['POST'])
def callback():
    return jsonify(parse_request_data())

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
