import os
import math
import re
import bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_login import login_required
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

# Flask Login



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
   
    results = mongo.db.tasks.find({"recipe_name" : {"$regex": query, "$options": "i"}})
 
    if results.count():
         return render_template('search.html', results=results, query=query, title="Search")        
    else:
        flash('No results were found', 'info')     
    return render_template('index.html')


# Filters

# Filter for course only

@app.route("/filtercourses") 
  
def filtercourses():
    """
    Allows user to filter through courses
    """
    filter = request.args.get('filter')
    filter_results = mongo.db.find({"recipe_course" : {"$regex": filter}}) 
    
    if filter_results.count():
        return render_template('filter.html', filter_results=filter_results, filter=filter, title="Filter")
    else:
        flash('No recipes were found matching that filter', 'info')
    return render_template('index.html')      
        

# Create Recipe

# Update Recipe

# Delete Recipe
    
    
    
# About

@app.route('/about')
def about():
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
        logged_in_user = user.find_one({'name': request.form['username'].title()})
    
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

@app.route('/register', methods=['GET','POST'])
def register():
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
            exist_user = user.find_one({'name': request.form.get('username').title()})
            print(exist_user)

            if exist_user is None:
                # If new user insert username, password and email into collection
                hash_pass = generate_password_hash(request.form.get('password'))
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
    session.clear()
    flash('You are successfully logged out', 'success')
    return render_template('index.html')
    

# Error Handling - 404 and 500


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
debug=True)