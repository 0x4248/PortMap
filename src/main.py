# PortMap
# A simple webpage that lists the ports you specify and their corresponding services for quick access.
# Github: https://www.github.com/lewisevans2007/PortMap
# Licence: GNU General Public License v3.0
# By: Lewis Evans

import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ports.json')
def ports():
    f = open('ports.json', 'r')
    return f.read()

@app.route('/style.css')
def style():
    f = open("src/css/style.css", "r")
    return  Response(f.read(), mimetype='text/css')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)