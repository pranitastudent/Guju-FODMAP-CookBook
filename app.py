import os
import math
import re
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId
from flask import session

# App Config 
app = Flask(__name__)

if os.path.exists('env.py'):
    import env
    
app.config["MONGO_DB"] = os.environ.get('MONGO_DB')   

app.config["MONGO_URI"] = os.environ.get('MONGO_URI') 

app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')

mongo = PyMongo(app)



# Routes

# Home Route

@app.route('/')
def index():
    
    # logic for pagination
    
    page_limit = 6
    current_page = int(request.args.get('current_page', 1))
    total = mongo.db.tasks.count()
    pages = range(1, int(math.ceil(total / page_limit)) + 1)
    tasks=mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip((current_page - 1)*page_limit).limit(page_limit)
    return render_template('index.html', tasks=tasks, title='Home', current_page=current_page, pages=pages)

# View Each Recipe

@app.route('/task/<task_id>')
def task(task_id):
    """
    Allows User to view the full
    individual recipe
    """
    task_count=mongo.db.tasks.count()
    return render_template('recipe.html', task_count=task_count, task=mongo.db.tasks.find_one({'_id':ObjectId(task_id)}))


# Search

@app.route("/findtask", methods=['GET', 'POST'])
def findtask():
    tasks=mongo.db.tasks
    if request.method == 'POST':
        requested_type = request.form.get("recipe_name")
        
        tasks = mongo.db.tasks.find({"recipe_name": requested_type})
        return render_template("index.html", tasks=tasks)
        
    return render_template("index.html")


# Filters

    
    
    
# About

@app.route('/about')
def about():
    return render_template('about.html')
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)