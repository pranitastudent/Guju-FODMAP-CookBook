import os
import math
import re
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import login_required
from flask_pymongo import PyMongo, pymongo
from forms import RegistrationForm, LoginForm, RecipeForm
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
    tasks = mongo.db.tasks.find().sort('_id', pymongo.ASCENDING).skip(
        (current_page - 1)*page_limit).limit(page_limit)
    return render_template('index.html', tasks=tasks, title='Home', current_page=current_page, pages=pages)

# View Each Recipe


@app.route('/task/<task_id>')
def task(task_id):
    """
    Allows User to view the full
    individual recipe
    """
    task_count = mongo.db.tasks.count()
    return render_template('recipe.html', task_count=task_count, task=mongo.db.tasks.find_one({'_id': ObjectId(task_id)}))


# Search

@app.route('/findtask')
def findtask():
    """
    Allows user to perform case insensitive matches
    for recipe names
    """
    query = request.args.get('query')

    # Partial Search and case insensitive search
    results = mongo.db.tasks.find(
        {"recipe_name": {"$regex": query, "$options": "i"}})

    if results.count():
        return render_template('search.html', results=results, query=query, title="Search")
    else:
        flash('No results were found', 'info')
    return render_template('index.html')


# Filters

# Filter for course only

@app.route('/filtercourses', methods=['GET', 'POST'])
def filtercourses():
    """
    Allows user to filter through
    courses
    """

# Request Post method
    if request.method == "POST":
        for i in request.form:
            if i == "recipe_course":
                # Filter through courses
                filter_items = []
                items = request.form.getlist("recipe_course")
                my_key = request.form
                # iterate through items and key
                for item in items:
                    for key in my_key:
                        # Append key and item together                        
                        filter_items.append({key: item})
                        results = mongo.db.tasks.find(
                            {'$and': [{'$or': filter_items}]})

    return render_template('filter.html', results=results, title="Filter")


# Filter Through Allergens

@app.route('/filterallergens', methods=['GET', 'POST'])
def filterallergens():
    """
    Allows user to filter through
    allergens
    """

# Request Post method
    if request.method == "POST":
        for i in request.form:
            if i == "allergen":
                # Filter through allergens
                filter_items = []
                # Put list into variable items
                items = request.form.getlist("allergen")
                my_key = request.form
                # iterate through items and key
                for item in items:
                    for key in my_key:
                        # attach key with items
                        filter_items.append({key: item})
                        results = mongo.db.tasks.find(
                            {'$and': [{'$or': filter_items}]})

    return render_template('filter.html', results=results, title="Filter")


# Add Recipe

@app.route('/create_task', methods=['GET', 'POST'])
def create_task():
    """Create a new recipe to db collection"""
    if 'logged_in' not in session:  # Check if its a logged in user
        flash('Sorry, only logged in users can create recipes. Please register')
        return redirect(url_for('index'))

    form = RecipeForm(request.form)  # Initialise the form
    print(form)
    
    user = mongo.db.user.find_one({"name": session['username'].title()})
    
    if form.validate_on_submit():  # Insert new recipe if form is submitted
       
       print(form.validate_on_submit)
        
       tasks = mongo.db.tasks
      
       # inserting into dict as required by mongodb
       tasks.insert_one({
            'recipe_name' : request.form.get['recipe_name'],
            'recipe_image' : request.form.get['recipe_image'],
            'serving_size' : request.form.get['serving_size'],
            'calories' : request.form.get['calories'],
            'description' : request.form.get['description'],
            'cooking_time' : request.form.get['cooking_time'],
            'instruction' : request.form.get['instruction'],
            'instruction1' : request.form.get['instruction1'],
            'instruction2' : request.form.get['instruction2'],
            'instruction3' : request.form.get['instruction3'],
            'instruction4' : request.form.get['instruction4'],
            'instruction5' : request.form.get['instruction5'],
            'instruction6' : request.form.get['instruction6'],
            'username': session['username'].title(),
            
        
         })
       flash ('Your Recipe has been added successfully', 'success')
       return redirect(url_for('index'))
    return render_template('add_recipe.html', form=form, title="Add Recipe")
                
            
  



# Update Recipe

# Delete Recipe


# Upvotes

@app.route('/upvotes/<task_id>', methods=['POST'])
def upvotes(task_id):
    """
    Allows User to upvote a specific 
    recipe
    """

    mongo.db.tasks.update_one(
        {'_id': ObjectId(task_id)},
        {'$inc': {'upvotes': 1}})
    return redirect(url_for('task', task_id=task_id))


# About

@app.route('/about')
def about():
    """
    Allows a user to view about me
    page
    """
    return render_template('about.html')

# Login- Code adapted from Pretty printed video


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Function for handling the logging in of users
    """

    # Check if user is logged in
    if 'logged_in' in session:
        return redirect(url_for('index'))
    form = LoginForm()

    # Check is form is valid and find user in database
    if form.validate_on_submit():
        user = mongo.db.user
        logged_in_user = user.find_one(
            {'name': request.form['username'].title()})

    # Check is user - password is hashed and does the password match
        if logged_in_user:
            if check_password_hash(logged_in_user['pass'],
                                   request.form['password']):
                session['username'] = request.form['username']
                session['logged_in'] = True

                # If password matches redirect to index
                flash('You are successfully logged in', 'success')
                return redirect(url_for('index'))
            # If not show message below and redirect to login
            flash('Sorry incorrect password!', 'danger')

            return redirect(url_for('login'))
        # If none of the form is valid or nothing matches username or password then redirect to login
        flash('Sorry Your credentials are incorrect (username) please check and try again', 'danger')
    return render_template('login.html', form=form, title='Login')


# Register- Code adapted from Pretty printed video- PyMongo Login/Register - Debugging aided by Tutor Tim Nelson

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Function for allowing  users to register"""
    form = RegistrationForm()
    # Check if user is already registered
    if request.method == 'GET':
        if 'username' in session:
            flash('You are already logged in!', 'success')
            return redirect(url_for('index'))
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = mongo.db.user
            # check existing username
            exist_user = user.find_one(
                {'name': request.form.get('username').title()})
            print(exist_user)

            if exist_user is None:
                # If new user insert username, password and email into collection
                hash_pass = generate_password_hash(
                    request.form.get('password'))
                user.insert_one({'name': request.form.get('username').title(),
                                 'pass': hash_pass})
                session['username'] = request.form.get('username')
                flash('You are successfully registered, Please log in!', 'success')
                return redirect(url_for('login'))
            else:
                flash('Sorry, username already taken. Please try another.', 'warning')
                return redirect(url_for('register', form=form, title='Register'))

        else:
            return redirect(url_for('register', form=form, title='Register'))

    return redirect(url_for('register', form=form, title='Register'))


# Logout

@app.route('/logout')
def logout():
    """
    Allowing users to logout
    """
    session.clear()
    flash('You are successfully logged out', 'success')
    return render_template('index.html')


# Error Handling - 404 and 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
