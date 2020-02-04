import os
import math
import re
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo, pymongo
from forms import RegistrationForm, LoginForm
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

@app.route('/findtask')
def findtask():
    """
    Allows user to perform full exact matches
    ro recipes
    """
    query = request.args.get('query')
    print(query)
    results = mongo.db.tasks.find({"recipe_name" : {"$regex": query, "$options": "i"}})
    print(results)
    if results.count():
         return render_template('search.html', results=results, query=query, title="Search")        
    else:
        flash('No results were found', 'info')     
    return render_template('index.html')


# Filters

# Create Recipe

# Update Recipe

# Delete Recipe
    
    
    
# About

@app.route('/about')
def about():
    return render_template('about.html')

# Login- Code adapted from Corey Schafer Flask Series

@app.route('/login')
def login():
    return render_template('login.html')


# Register- Code adapted from Corey Schafer Flask Series

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if user is already registered
    if 'logged_in' in session:
        flash('You are already logged in!', 'success')
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():        
        user = mongo.db.user
                   
        # check existing username    
        exist_user = user.find_one({'name': request.form['username'].title()})
        
        if exist_user is None:
        # If new user insert username, password and email into collection    
            hash_pass = generate_password_hash(request.form['password'])
            user.insert_one({'name': request.form['username'].title(),
                             'pass': hash_pass})
            session['username'] = request.form['username']
            session['logged_in'] = True
            return redirect(url_for('index'))
        flash('Sorry, username already taken. Please try another.', 'warning')
        return redirect(url_for('register'))
    return render_template('register.html', form=form, title='Register')



# Logout

@app.route('/logout')
def logout():
    flash('You are successfully logged out', 'success')
    return render_template('index')
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
debug=True)