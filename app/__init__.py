# Import flask and template operators
from flask import Flask, render_template, jsonify
from flask import request
from app.helper.converter import insertDb
import os
from flask_cors import CORS


# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Define the WSGI application object
app = Flask(__name__, static_url_path='/static')
cors = CORS(app)
# Configurations
app.config.from_object('config')
db = SQLAlchemy(app)



files = os.listdir('CS')
client = app.config["CLIENT"]
otherParty = app.config["OTHER_PARTY"]
final_data = insertDb(client, otherParty)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/merge')
def merge():
    id = request.args.get('id')
    for data in final_data:
        if data[4] == int(id):
            data[3] = "MERGED"
    return "success"


@app.route("/results")
def index():
    ## get the last date the webscraper was ru
    size = request.args.get('size')
    page = request.args.get('page')
    tradeDate = request.args.get('trade')
    setllDate = request.args.get('settl')
    currency = request.args.get('currency')
    rate = request.args.get('rate')
    status = request.args.get('status')
    
    return_data = final_data
    if status != None and status != "":
        return_data=[data for data in final_data if data[3] == status]
    
    if tradeDate != None and tradeDate != "":
        dateSplit = tradeDate.split('-')
        dateSplit = "/".join([dateSplit[2], dateSplit[1], dateSplit[0]])
        return_data=[data for data in return_data if data[0]['30T'] == dateSplit or data[1]['30T'] == dateSplit]

    if setllDate != None and setllDate != "":
        dateSplit = setllDate.split('-')
        dateSplit = "/".join([dateSplit[2], dateSplit[1], dateSplit[0]])
        return_data=[data for data in return_data if data[0]['30V'] == dateSplit or data[1]['30V'] == dateSplit]

    if rate != None and rate != "":
        return_data=[data for data in return_data if data[0]['36'] == rate or data[1]['36'] == dateSplit]

    if currency != None and currency != "":
        return_data=[data for data in return_data if data[0]['32B'][1] == currency or data[0]['33B'][1] == currency or data[1]['32B'][1] == currency or data[1]['33B'][1] == currency]
    
    
    if size == None:
        size = 10
    if page == None:
        page = 0
    size = int(size)
    page = int(page)
    return jsonify(return_data[page*size:page*size + size])



