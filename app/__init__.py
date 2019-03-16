# Import flask and template operators
from flask import Flask, render_template
from app.helper.converter import insertDb
import os

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

db = SQLAlchemy(app)


files = os.listdir('CS')
client = app.config["CLIENT"]
otherParty = app.config["OTHER_PARTY"]
insertDb(client, otherParty)



