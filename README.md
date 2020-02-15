[DEPLOYED WEBSITE](http://guju-cookbook-fodmap.herokuapp.com/)

# Data Centric  Milestone Project-Gujarati FODMAP Cookbook - Milestone 4 Project 

## Project Entrails and Purpose

<p> A Gujarati FODMAP Cookbook is being created for the Data Centric Project. It is difficult to find FODMAP friendly Gujarati Recipes hence as personal issue this project is being created. A User who wishes to find Gujarati FODMAP friendly recipes will be able to use the site to do so . The user will be a user looking for Gujarati FODMAP friendly recipes. The user will be able to view recipes for all three courses; starters, mains and deserts ( all which are FODMAP friendly).   The user will be able to view the recipe steps for each recipe, the cooking time , serving size and calorie count for all recipes. The user will be able to register and login into the site. The login privilege will allow the user to add there own recipe, delete and edit only there own recipe. All users will be able to like recipes and hence upvote. Logged in users will only be able to create, update and delete their won recipes. A non-logged in user will only be able to view recipes. In addition the user will be able to view the author's story about the  reason for the creation of a Gujarati FODMAP friendly site under the about section. </p>

## UX Design - User Experience
<br>

<p> The Header and Footer and main primary colour of the site is blue. Blue is used as the official Monash FODMAP app is blue and is associated with FODMAP.
 The user regardless of being logged in should be able to view all recipes of all courses and each recipe individually which details the method, ingredients, photo of finished dish, upvotes , cooking time, serving size, course of the recipe. In addition if a user creates a recipe then there name is added as author of that recipe. The user should be able to register and login in securely using the authentication process. The logged in user will be able to create, update and delete their own recipes.  
The user must be able to search for a recipe using 'keywords' in the search bar and a result pertaining to the search will appear. A user will be able to filter through the recipes using the two filters: Course Labels (Starter, Main, Desert) and Allergens ( Soy, Eggs etc) Pagination is added to the site and a total of six recipes can be viewed at any one time. The web application fulfils the CRUD operations</p>

### CRUD

#### Create
<p> A logged in user is able to create a recipe through filling in the add recipe form. The data entered is added to MongoDB database collection.</p>

#### Read
<p> All users despite being logged in or not are able to view all recipes and single recipe pages.</p>


#### Update

<p> A logged in user is able to edit there own recipe through the edit recipe form. If they try to edit another author's recipe, an alert is flashed up 'Sorry this is not your recipe to update' warning them they can only edit there own recipes. The updated data is saved to again to the MongoDB database collection. Names of the authors are visible on each recipe page making it easy to identify  recipes.</p>

#### Delete
<p> A logged in user is able to delete there own recipe by clicking on the delete button and then again to confirm deletion is required. If they try to delete a recipe where they are not the author, an alert is flashed up 'Sorry this is not your recipe to delete' warning them they can only delete there own recipes. The  deleted record removed from the MongoDB database collection. Names of the authors are visible on each recipe page making it easy to identify  recipes.</p>

## User Stories

<ul>
<li> As a user to the site I should view a responsive site on ; desktop, mobile, tablet and large screens</li> 
<li> As a user to the site I should be able to view all recipes available. I should be able to view the recipe steps, cooking time, serving portion and calorie count for all recipes.</li>
<li> As a user I should be able to register on the website and login</li>
<li> As a user I should be able to search for a recipe using keywords and the relevant results must show </li>
<li> As a user I must be able to filter through the recipes using the filters and results pertaining to my filter choices must show.
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
<li> Home page- Able to view all recipes and individual recipe pages. Search through partial/full recipe names and filter through course and allergens for recipe of choice.  Moving through the collection of recipes using the pagination links at the bottom of the page.
<li> About Page- View the page to find out why the site was created and who created it </li>
<li> Register - Able to register through filling out registration form </li>
<li> Login- Able to login once registered through filling out login form <li>

</ul>

### Logged in user

</p> A logged in user is able to access the following links the navbar</p>

<ul>

<li> Add Recipe - A logged in user can create a recipe through the add recipe form </li>
<li> Logout - A logged in user can logout</li>
<li> Home page- Able to view all recipes and individual recipe pages. Search through partial/full recipe names and filter through course and allergens for recipe of choice. Moving through the collection of recipes using the pagination links at the bottom of the page.</li>
<li> Recipe page- A logged in user can edit there own recipe through clicking Edit on the recipe page - filling out the form and delete their own recipe through clicking delete on the recipe page.
<li> About Page- View the page to find out why the site was created and who created it </li>

</ul>

### Features left to implement

<ul>
<li> A reset password facility whereby user can click on reset password , have an email sent to them which contains a reset form link. The user can them enter there new password twice and it is updated in the user collection in MongoDB. </li>

## Technologies Used

<p> The Data Centric will include the following Front-End Technologies; HTML,CSS and JavaScript. The Back-End code will be written in Python. The non-relational database MongoDB will be used to store data for the recipes, and registered users.

### IDE

<ul>
<li><a href="https://code.visualstudio.com/">Visual Studio Code</a></li>Visual Studio Code was used as the chosen IDE and all code was written in Visual Studio Code.
</ul>

### Version Control

<ul>
<li><a href = "https://git-scm.com/">Git</a></li>Git is used as a version control system to add, commit and push files to the local repository.
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

<p> MongoDB is a documented orientated database where data is stored in key and field format(BSON). A database and collections are created. To app.py the following Config Variables are added to connect to the database , these are then stored an environmental variables and added to Heroku Config Variables section:

` app.config["MONGO_DBNAME]='DBNAME `
` app.config["MONGO_URI]= mongosrv added `

### Deployment
<ul>
<li><a href="https://id.heroku.com/login">Heroku</a></li>Heroku is used in production to host the live website and contains all the config variables that are need to run the site.
</ul>

### Testing Code

#### Python

<p> All python code is autopep8 and pep8 compliant




## Testing User Stories

## Deployment

## Credits

## Acknowledgements