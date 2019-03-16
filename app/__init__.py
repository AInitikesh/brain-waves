# Import flask and template operators
from flask import Flask, render_template, jsonify
from flask import request
from app.helper.converter1 import insertDb
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


@app.route("/results")
def index():
    ## get the last date the webscraper was ru
    size = request.args.get('size')
    page = request.args.get('page')
    date = request.args.get('date')
    status = request.args.get('status')
    
    return_data = final_data
    if status != None and status != "":
        print(status)
        return_data=[data for data in final_data if data[3] == status]
    
    if size == None:
        size = 10
    if page == None:
        page = 0
    size = int(size)
    page = int(page)
    return jsonify(return_data[page*size:page*size + size])



