from crypt import methods
from flask import Flask, render_template, request, jsonify, make_response

from datetime import datetime

import json, requests

app = Flask(__name__)

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/localstats', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        with open('/home/peter/p2pool_api/local/stats') as file:
            data = json.load(file)
        return jsonify(data)
    else:
        return "No JSON received", 400

@app.route('/moneroprice', methods = ['GET'])
def cyptoprice():
    if(request.method == 'GET'):
        url = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=monero")
        text = url.text

        data = json.loads(text)

        return jsonify(data)

     # https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=monero
     

@app.route("/poolstats")
def poolstats():
    return render_template("poolstats.html")
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')
