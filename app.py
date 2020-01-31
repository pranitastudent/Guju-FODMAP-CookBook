import os
import math
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

# Index(Home) Route
@app.route('/')
def index():
    # Logic for pagination
    page_limit = 6 
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.task.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks=mongo.db.tasks.find()..sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('index.html',task=tasks, title='Home', current_page=current_page, pages=pages )
    
# View Recipe Route



if __name__=='__main__':
    app.run(debug=True)
    
    