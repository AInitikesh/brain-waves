# Import flask and template operators
from flask import Flask, render_template, jsonify
from flask import request
from app.helper.converter import insertDb
import os
from flask_cors import CORS
import datetime 


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
    tradeDateFrom = request.args.get('tradeFrom')
    tradeDateTo = request.args.get('tradeTo')
    setllDateFrom = request.args.get('settlFrom')
    setllDateTo = request.args.get('settlTo')
    currency = request.args.get('currency')
    rate = request.args.get('rate')
    status = request.args.get('status')
    
    return_data = final_data
    if status != None and status != "":
        return_data=[data for data in final_data if data[3] == status or data[3] == "MERGED"]
    
    if tradeDateFrom != None and tradeDateFrom != "":
        dateSplit = tradeDateFrom.split('-')
        d1 = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        temp_return = []
        for data in return_data:
            dataDate = data[0]['30T'].split('/')
            if len(dataDate) == 3:
                d2 = datetime.datetime(int(dataDate[2]), int(dataDate[1]), int(dataDate[0]))
                if d1 < d2:
                    temp_return.append(data)
        return_data = temp_return

    if tradeDateTo != None and tradeDateTo != "":
        dateSplit = tradeDateTo.split('-')
        d1 = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        temp_return = []
        for data in return_data:
            dataDate = data[0]['30T'].split('/')
            if len(dataDate) == 3:
                d2 = datetime.datetime(int(dataDate[2]), int(dataDate[1]), int(dataDate[0]))
                if d2 < d1:
                    temp_return.append(data)
        return_data = temp_return

    if setllDateFrom != None and setllDateFrom != "":
        dateSplit = setllDateFrom.split('-')
        d1 = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        temp_return = []
        for data in return_data:
            dataDate = data[0]['30V'].split('/')
            if len(dataDate) == 3:
                d2 = datetime.datetime(int(dataDate[2]), int(dataDate[1]), int(dataDate[0]))
                if d1 < d2:
                    temp_return.append(data)
        return_data = temp_return

    if setllDateTo != None and setllDateTo != "":
        dateSplit = setllDateTo.split('-')
        d1 = datetime.datetime(int(dateSplit[0]), int(dateSplit[1]), int(dateSplit[2]))
        temp_return = []
        for data in return_data:
            dataDate = data[0]['30V'].split('/')
            if len(dataDate) == 3:
                d2 = datetime.datetime(int(dataDate[2]), int(dataDate[1]), int(dataDate[0]))
                if d2 < d1:
                    temp_return.append(data)
        return_data = temp_return


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



