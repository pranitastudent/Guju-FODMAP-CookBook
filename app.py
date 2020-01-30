import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# App Config 
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')

app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

SECRET_KEY = os.urandom(32)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

# Routes

@app.route('/')
def index():
    return '<h1>Hello World</h1>'
    


if __name__=='__main__':
    app.run(debug=True)