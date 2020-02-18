[DEPLOYED WEBSITE](http://guju-cookbook-fodmap.herokuapp.com/)

# Data Centric  Milestone Project-Gujarati FODMAP Cookbook - Milestone 4 Project 

## Project Entrails and Purpose

<p> A Gujarati FODMAP Cookbook is being created for the Data Centric Project. It is difficult to find FODMAP friendly Gujarati Recipes hence as personal issue this project is being created. A User who wishes to find Gujarati FODMAP friendly recipes will be able to use the site to do so . The user will be a user looking for Gujarati FODMAP friendly recipes. The user will be able to view recipes for all three courses; starters, mains and deserts ( all which are FODMAP friendly).   The user will be able to view the recipe steps for each recipe, the cooking time , serving size and calorie count for all recipes. The user will be able to register and login into the site. The login privilege will allow the user to add their own recipe, delete and edit only their own recipe. All users will be able to like recipes and hence upvote. Logged in users will only be able to create, update and delete their own recipes. A non-logged in user will only be able to view recipes. In addition the user will be able to view the author's story about the  reason for the creation of a Gujarati FODMAP friendly site under the about section.<strong> Please note that this website is only for educational purposes to fulfil the criteria of Milestone Data Centric Project.</strong></p>

## UX Design - User Experience
<br>

<p>The Header and Footer and main primary colour of the site is blue. Blue is used as the official Monash FODMAP app is blue and is associated with FODMAP.
 The user regardless of being logged in should be able to view all recipes of all courses and each recipe individually which details the method, ingredients, photo of finished dish, upvotes , cooking time, serving size, course of the recipe. In addition if a user creates a recipe then their name is added as author of that recipe. The user should be able to register and login in securely using the authentication process. The logged in user will be able to create, update and delete their own recipes.  
The user must be able to search for a recipe using 'keywords' in the search bar and a result pertaining to the search will appear. A user will be able to filter through the recipes using the two filters: Course Labels (Starter, Main, Desert) and Allergens ( Nuts, Eggs etc). Pagination is added to the site and a total of six recipes can be viewed at any one time. The web application fulfils the CRUD operations.</p>

### CRUD

#### Create

<p> A logged in user is able to create a recipe through filling in the add recipe form. The data entered is added to MongoDB database collection.</p>

#### Read

<p> All users despite being logged in or not are able to view all recipes and single recipe pages.</p>


#### Update

<p> A logged in user is able to edit their own recipe through the edit recipe form. If they try to edit another author's recipe, an alert is flashed up 'Sorry this is not your recipe to update' warning them they can only edit their own recipes. The updated data is saved to again to the MongoDB database collection. Names of the authors are visible on each recipe page making it easy to identify  recipes.</p>

#### Delete
<p> A logged in user is able to delete their own recipe by clicking on the delete button and then again to confirm deletion is required. If they try to delete a recipe where they are not the author, an alert is flashed up 'Sorry this is not your recipe to delete' warning them they can only delete their own recipes. The  deleted record removed from the MongoDB database collection. Names of the authors are visible on each recipe page making it easy to identify  recipes.</p>

## User Stories

<ul>
<li> As a user to the site I should view a responsive site on ; desktop, mobile, tablet and large screens.</li> 
<li> As a user to the site I should be able to view all recipes available. I should be able to view the recipe steps, cooking time, serving portion and calorie count for all recipes.</li>
<li> As a user I should be able to register on the website and login.</li>
<li> As a user I should be able to search for a recipe using keywords and the relevant results must show. </li>
<li> As a user I must be able to filter through the recipes using the filters for course and allergens and results pertaining to my filter choices must show.</li>
<li> As a logged in user I should be able to edit, delete and create my recipes. My own recipes can only be edited and deleted.</li>
</ul>


## Wireframes

<p>The wireframes for the Date Centric Milestone Project- Gujarati FODMAP CookBook - Milestone 4 Project project were created using Balsamiq. Mocks-ups were produced for desktop and mobile versions.</p>

[WireFrames](wireframes/milestone.pdf)

## Database Schema

A database schema is provided so that I can visualise the table.
[Database_Schema](schema/Schema.pdf)


## Features

### Non-logged in user

<p>A non logged in user is able to access the following links on the navbar:</p>

<ul>
<li> Home page- Able to view all recipes and individual recipe pages. Search through partial/full recipe names and filter through course and allergens for recipe of choice.  Moving through the collection of recipes using the pagination links at the bottom of the page.</li>
<li> About Page- View the page to find out why the site was created and who created it. </li>
<li> Register - Able to register through filling out registration form. </li>
<li> Login- Able to login once registered through filling out login form. <li>

</ul>

### Logged in user

</p> A logged in user is able to access the following links the navbar.</p>

<ul>

<li> Add Recipe - A logged in user can create a recipe through the add recipe form. </li>
<li> Logout - A logged in user can logout.</li>
<li> Home page- Able to view all recipes and individual recipe pages. Search through partial/full recipe names and filter through course and allergens for recipe of choice. Moving through the collection of recipes using the pagination links at the bottom of the page.</li>
<li> Recipe page- A logged in user can edit their own recipe through clicking Edit on the recipe page - filling out the form and delete their own recipe through clicking delete on the recipe page.
<li> About Page- View the page to find out why the site was created and who created it.</li>

</ul>

### Features left to implement

<ul>
<li> A reset password facility whereby user can click on reset password , have an email sent to them which contains a reset form link. The user can them enter their new password twice and it is updated in the user collection in MongoDB.</li>
</ul>

## Technologies Used

<p> The Data Centric will include the following Front-End Technologies; HTML,CSS and JavaScript. The Back-End code will be written in Python. The non-relational database MongoDB will be used to store data for the recipes, and registered users.</p>

### IDE

<ul>
<li><a href="https://code.visualstudio.com/">Visual Studio Code</a></li>Visual Studio Code was used as the chosen IDE and all code was written in Visual Studio Code.</li>
</ul>

### Version Control

<ul>
<li><a href = "https://git-scm.com/">Git</a></li>Git is used as a version control system to add, commit and push files to the local repository.</li>
</ul>

### Front-end Technologies and Frameworks

<ul>
<li><a href="https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5"> HTML5 </a></li> HTML 5 was used to create the structure of webpage with the necessary elements.
<li><a href="https://www.w3.org/Style/CSS/Overview.en.html"> CSS3 </a></li> CSS3 was used to write custom CSS styles the webpage with the necessary attributes.
<li><a href="https://getbootstrap.com/"> Bootstrap v 4.4 </a> </li>  The Bootstrap framework is used to style the webpage alongside custom CSS and the grid system is adhered to.
<li><a href ="https://www.javascript.com/">JavaScript</a></li> JavaScript was used to write the function for year code.
<li><a href = "https://jquery.com/">JQuery</a></li>JQuery is used to create the back-to-the top button function and animate fadeout function for the alerts.
<li><a href="https://fontawesome.com/">Font Awesome</a></li> Font Awesome is used to add icons to text to make it visually appealing.
</ul>

### Back-end Technologies and Frameworks

<ul>
<li><a href = "https://www.python.org/">Python</a></li> Python is used as the back-end coding language to write functions and enable 'GET' and 'POST' requests.
<li><a href="https://www.fullstackpython.com/flask.html">Flask</a></li>Flask is microframework of python used to create routes and forms.
<li><a href = "https://jinja.palletsprojects.com/en/2.10.x/">Jinja</a></li>Jinja is a templating language which works alongside python and flask to create templates.
</ul>

### Database

<ul>
<li><a href="https://www.mongodb.com/">MongoDB</a></li>MongoDB is a non-relational document orientated database which is used to store the tasks(recipe) collections and user collection.
</ul>

#### MongoDB

<p> MongoDB is a documented orientated database where data is stored in key and field format(BSON). A database and collections are created. To app.py the following Config Variables are added to connect to the database , these are then stored an environmental variables and added to Heroku Config Variables section:</p>

` app.config["MONGO_DBNAME]='DBNAME `
` app.config["MONGO_URI]= mongosrv added `

<p> A tasks collection and user collection was created under the task_manager database with the fields and field types outlined in the Database Scheme.
In the user collection, each record for a user,  the password was hashed in the registration function using werkzeug security. The password is stored as a hashed password in the Mongo database.</p>

### Deployment
<ul>
<li><a href="https://id.heroku.com/login">Heroku</a></li>Heroku is used in production to host the live website and contains all the config variables that are need to run the site.
</ul>

### Testing Code

#### Python

<p> Python code is tested via unit testing. Unit Testing is carried out to check whether a recipe exists in the database through testing its ObjectID. The login, register and logout routes are tested to assert whether a HTTP Response of 200 is obtained. All 9 unit tests were found to pass.</p>

<p> Unit tests were run in the terminal using the following command: </p>

`python -m unittest test.py`

<p>An example of recipe existence unit test is shown below: </p>

```
    def test_task(self):
        # Test a particular recipe description
        tester = app.test_client(self)
        response = tester.get(
            '/task/{}'.format("5e33ff3c1c9d440000bcfe4d"),
            content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b"Take 1 cup gram flour" in response.data)

```

<p> Python code was validated fully  using pep8 and autopep8.</p>

#### HTML and CSS

<ul>

<li> HTML was validated using:

[WC3 MarkUp Validation Service](https://validator.w3.org/). W3C Validator does not recognise the Jinja templating language. No Errors were found.</li>

<li> CSS was validated using:

[WC3 CSS Validation Service](http://jigsaw.w3.org/css-validator/). W3C Validator does not recognise the CSS Route variables. No Errors were found. </li>

</ul>


#### JavaScript 

<p> JavaScript was validated using: </p>

[JS Hint](https://jshint.com/). No Errors were found.

### Testing User Stories

<ul>
<li> A non-logged user interested in Gujarati LOW-FODMAP recipes is able to view all recipes noting the course and allergen and each individual recipe to ascertain : cooking time, course, serving size, calories , method , description and see an image of the dish produced. </li>
<li> A non-logged in user can register through the registration form and login. Google reCAPTCHA is present on the login form as an extra security measure. The password is hashed using werkzeug security as a security measure and the password is checked against the one in the database using werkzeug. </li>
<li> All users are permitted to search for a recipe through inserting a partial recipe name e.g 'Gluten' , all recipes with Gluten in their recipe name will show up or by full name to find the recipe of interest.</li>
<li> All users can filter for a recipe by course e.g 'Main' , all main courses will appear on the results page and filter by allergen 'Nuts'. All recipes with Nuts as an allergen will appear to find the recipe of choice.</li>
<li> A logged in user is able to complete all CRUD operations. These included : </li>

</ul>

#### Create
<p> A logged in user can create a recipe through filling out the add recipe form. Each Field through the placeholder makes it clear which information to required. If a required field is missing then the form will not be submitted and the user is directed to the field which contains the missing information (form validation). In addition Google reCaptcha is inserted  as a extra security measure.</p>

#### Read

<p> All users can read all the recipes on the website. </p>

#### Update

<p> A logged user can edit/update their own recipe (defensive design). If a user tries to update a recipe that does not belong to them, then an alert appears informing them that they can't update that particular recipe. In addition Google reCaptcha is inserted  as a extra security measure.</p>


#### Delete

<p> A logged user can only delete their own recipe (defensive design). Additionally a user is asked twice to confirm deletion as a confirmation measure.If a user tries to delete a recipe that does not belong to them, then an alert appears informing them that they can't update that particular recipe.</p>

### Testing Responsive Design

<p> The website is fully responsive on desktop, laptop, tablet and mobiles devices. The website was tested on the following browsers: Google Chrome, Mozilla Firefox, Opera and Microsoft Edge and found to fully functioning. The Bootstrap grid system was adhered to allowing fully responsive design.</p>

<p> The website was tested on the following devices: </p>

<ul>
<li> Desktop </li>
<li> Laptop with HiDPI</li>
<li> Laptop with MDPI </li>
<li> Pixel 2 </li>
<li> Pixel 2L </li>
<li> Galaxy S5 </li>
<li> iPhone 5/SE </li>
<li> iPhone 6/7/8 </li>
<li> iPhone 6/7/8 plus </li>
<li> iPhone X </li>
<li> iPad </li>
<li> iPad Mini </li>
<li> iPad Pro </li>
</ul>

<p> On mobile devices elements are stacked on top of each other as expected accordingly to the grid system.</p>

### Testing the application on the development and production server.

<p> All links were tested on the production and development server. All were found to be working. Alerts were tested and found to working. Users could register and login and add and edit recipes using the forms as expected. User added recipes were visible on both development and production servers. Google reCAPTCHA  is implemented on login, add and edit forms was found to working on the local and production server - Heroku as expected. Debug was set to False when on production server as a security measure.</p>

## Deployment

### IDE

<p> Code was written in Visual Studio Code. </p>

### Git and GitHub

<p> The code was pushed to GitHub using Git. Git was used a version Control. The GitHub repository

[Milestone_4_project](http://guju-cookbook-fodmap.herokuapp.com/) was created. </p>

#### Running the project from GitHub

<ol>

<li> Manually download or clone the project from GitHub to your IDE of your choice.</li>
<li> Make sure Python is installed with versions 3+ on your machine. </li>
<li> Install a virtual environment. </li>
<li> Activate a virtual environment. </li>
<li> Download all the dependencies using the command: </li>

 `pip install -r requirements.txt` </li>

 <li> Create and env.py file on the root level and set up environmental variables. Contact the author allow for there environmental variables to be inserted otherwise your own database and collection can be created in MongoDB with the fields specified in the Schema above. </li>

 <li> Google reCAPTCHA credentials can be obtained through setting up a Google account and following through the instructions and inserting the domain name where the site will be run.</li>

 `os.environ["MONGO_DBNAME"] = 'databasename'`
 `os.environ["MONGO_URI"] = 'mongosrv added `
 `os.environ["SECRET_KEY"] = 'secretkey` 
 `os.environ["RECAPTCHA_PUBLIC_KEY"] = key `
 `os.environ["RECAPTCHA_PRIVATE_KEY"] = key `

 <li> The flask app is run through entering the command in the bash terminal : </li>

 ` flask run `

</ol>

#### Deploying to Heroku

<p> The application was deployed to Heroku.</p>

<ol>
<li> A requirements.txt file (contains dependencies needed to for application to run) was created using the command :

` sudo pip3 freeze --local > requirements.txt ` . A requirements.txt file was created at the root level of the project folder. </li>

<li> A Procfile was created in order for Heroku to recognise the python language using the command : 

` echo web: python app.py > Procfile ` </li>

<li> Both these files are added and committed and pushed up to GitHub. </li>
<li> The

 `heroku login` command is used to login to Heroku. A unique app name is added in Heroku and the region of choice is chosen. </li>

<li> Under the Settings > Config Vars. The environmental variables for : MONGO_DB, MONGO_URI, SECRET_KEY, RECPATCHA_PUBLIC, RECAPTCHA_PRIVATE  are inserted respectively into the key and value fields.</li>

<li> Next the project is pushed to Heroku using the command : 

` git push heroku master `. The push should be displayed as successful.</li>

<li> Next to run the app the command:

`heroku ps:scale web=1` is used. </li>


<li> Additionally the IP has to specified and PORT. Hence :

` IP : 0.0.0.0.`
` PORT : 5000` are inserted as key and value fields in Config Vars on Heroku.</li>

<li> The 'open app' on the top right can be clicked and the application should be fully visible and functioning.

The application is finally deployed at [guju-cookbook-fodmap](https://guju-cookbook-fodmap.herokuapp.com/)

</li>

</ol>


## Credits

<strong> All images and recipe instructions are used for educational purposes for the Data Centric Project and therefore don't need to be referenced.
</strong>

### References 

<ol>

<li> Pagination Code taken from: 

[Recipe App S.MuriHead- Under MIT License and acknowledgement provided in Code 2019](https://github.com/ShaneMuir/Cookbook-Recipe-Manager) and

[Code with Harry 2018](https://www.youtube.com/watch?v=JqS6BcgeUMw) </li>

<li> 

[Pretty Printed Flask for Beginners Course 2018](https://courses.prettyprinted.com/p/the-flask-bundle)

</li>

<li> Login and Register code adapted from:

[Creating a User Login System Using Python, Flask and MongoDB 2016](https://www.youtube.com/watch?v=vVx1737auSE)
</li>

<li> Filter Code adapted and taken from :

[Recipe App S.MuriHead- Under MIT License and acknowledgement provided in Code 2019](https://github.com/ShaneMuir/Cookbook-Recipe-Manager)

</li>

<li>

 [Code Institute Lectures and Task Project - Data Centric Module](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/info)

 </li>

 <li> Top Bar Adapted from:

 [Python Django Dev to Development Traversy Media](https://www.traversymedia.com/)

 </li>

 <li>

 Error handling pages code adapted from :
 
 [Corey Schafer Python Flask Tutorial: Full-Featured Web App Part 12 - Custom Error Pages](https://www.youtube.com/watch?v=uVNfQDohYNI&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=13&t=0s)

 </li>

 <li>

 [Bootstrap 4](https://getbootstrap.com/)

 </li>

 <li>

 Select box CSS adapted from:

 [Styling a Select Like It’s 2019](https://css-tricks.com/styling-a-select-like-its-2019/)

 </li>

 <li>

 Back to the top button adapted from :

 [Responsive Landing Page Using HTML & CSS (A Little jQuery)-myTunes site Traversy Media 2018](https://www.youtube.com/watch?v=GJXXf3_dcng)

 </li>

 </ol>

## Acknowledgements

<p> Thank-you to the Developers of The FODMAP Monash Application who provided me the inspiration to create a Gujarati Low-FODMAP cookbook.

 Thank-you to all the tutors at Code Institute especially: Tim, Xavier, Kevin and Stephen for all there help in providing suggestion to debug code.</p>