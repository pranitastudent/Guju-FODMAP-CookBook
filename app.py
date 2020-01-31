import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

# App Config 
app = Flask(__name__)

if os.path.exists('env.py'):
    import env
    
app.config["MONGO_DB"] = os.environ.get('MONGO_DB')   

app.config["MONGO_URI"] = os.environ.get('MONGO_URI') 

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)

# 'mongodb+srv://root:RootUser@myfirstdatabase-klrg6.mongodb.net/GujuCookBook?retryWrites=true'

# Routes

@app.route('/')
def index():
    
    tasks=mongo.db.tasks.find().limit(6)
    return render_template('index.html', tasks=tasks)
    


if __name__=='__main__':
    app.run(debug=True)