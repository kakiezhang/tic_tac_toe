# -*- encoding: utf8 -*-

from pentball import app
from flask import abort, jsonify, request


@app.route('/')
@app.route('/home')
def home():
    return jsonify({"status": "ok"})
