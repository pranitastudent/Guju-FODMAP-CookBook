import os
import math
import re
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user, login_required
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
    query = request.args.get('q')
    results = mongo.db.tasks.find({"recipe_name" : {"$regex": query}})   
    return render_template('search.html', results=results, query=query, title="Search")


# Filters

# Create Recipe

# Update Recipe

# Delete Recipe
    
    
    
# About

@app.route('/about')
def about():
    return render_template('about.html')

# Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            return redirect(url_for('index'))
        flash('You are successfully logged in', 'success')
        
        else:
            flash('Your password or username is incorrct. Please check', 'danger')
            
    return render_template('login.html', title='Login', form=form)

# Register- Code adapted from Corey Schafer Flask Series

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# Logout

@app.route('/logout')
def logout():
    flash('You are successfully logged out', 'success')
    return render_template('index')
    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
debug=True)