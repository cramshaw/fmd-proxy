#!flask/bin/python

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Proxy"

@app.route('/<path:code>')
def proxy(code):
    headers = {'Authorization' : request.headers['Authorization']}
    r = requests.get(code, headers=headers)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run()