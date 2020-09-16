from flask import render_template, redirect
from flask import request
import request_verification_api as a
import os
import requests
from flask import Flask
from api import AuthenteqApi
from jinja2 import Template
import jinja2

app = Flask(__name__)
app.config['CLIENT_ID'] = os.environ.get('CLIENT_ID')
app.config['CLIENT_SECRET'] = os.environ.get('CLIENT_SECRET')

REDIRECT_URL = 'http://127.0.0.1:5000/results'

# Credentials from admin dashboard stored in environmental variable
CLIENT_ID = app.config['CLIENT_ID']
CLIENT_SECRET = app.config['CLIENT_SECRET']

request_verification_url = "https://api.app.authenteq.com/web-idv/verification-url?redirectUrl={}".format(REDIRECT_URL)


# home page
@app.route('/')
def start():
    return render_template('index.html')


@app.route('/results', methods=["GET"])
def verification_page():
    verification = AuthenteqApi()
    return verification.verification_result()


if __name__ == "__main__":
    app.run(debug=True)