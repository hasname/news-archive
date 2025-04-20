#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/robots.txt')
def index():
    return 'User-agent: *\nDisallow: /', 200, {'Content-Type': 'text/plain'}
