# Pur Beurre, that's a fat life
----------------
Pur Beurre is a web application using the open database provided by [Open Food Facts](https://world.openfoodfacts.org/).
By using Pur Beurre, you'll be able to find a substitute for a food product, with better nutritive grades and higher 
quality. The program also gives you the possibility of creating an user account to save all your search results.


# What does Pur Beurre really do ?
----------------
Once you arrive on the [Pur Beurre application page](https://gp-bot-app.herokuapp.com/) :\
	- you can make a simple request by using the query form, then visualize the results \
	- you can create an account and then log in to be able to save your future search results

Pur Beurre is hosted by [Heroku](https://www.heroku.com/), and for now is only available in french language.	

# For developpers, how to install and work on the app :
--------------
Clone with https : https://github.com/Nastyflav/App_Pur_Beurre_OC.git \
or clone with SSH : git@github.com:Nastyflav/App_Pur_Beurre_OC.git \
into a repo on your local machine \
Documentation about pull --> https://help.github.com/en/articles/cloning-a-repository 

Set your virtual environment under python3.8.x `pip install virtualenv`\
Create an new virtual environment `virtualenv -p python env`\
Activate it `source env/Scripts/activate.bat`\
Install requirements `pip install -r requirements.txt`

## Dependancies :

Python 3.8.2 \
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/ 

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

## Modules :

app_purbeurre (main project)\
app_purbeurre/authentication/ user profiles, sign in, log in and out functionalities\
app_purbeurre/save/ products saving functionalities\
app_purbeurre/search/ products searching and printing functionalities\
app_purbeurre/static/ all the static files, with Boostrap, JQuery, Java Script, images and css/sass libraries\
app_purbeurre/templates/ all the basics and home html templates

## Built with :

Visual Studio Code (IDE)\
Python 3.8.2\
UTF-8

## Author :

Flavien Murail : https://github.com/Nastyflav


# How does Pur Beurre works ?
----------------

This application uses the Open Food Facts API to offer a large amount of food products, divided in 15 categories, so the user can find as many substitutes as possible for his daily life.
All the products are ranked by their Nutriscore grade, which goes from A (high quality) to E. The products with the highest ranking are those less transformed by the industry, healthy and with good nutritional intakes.\
More informations about the Open Food Facts Nutriscore notation [here](https://fr.openfoodfacts.org/nutriscore).

## 1. Create an account

The user needs to create an account to be able to save his researches, otherwise he will just be able to consult the products catalog.\
Email (as username) and password are required, firstname and lastname are optionals.

## 2. Log in your account

By clicking on the log in icon, the user is invited to fill in the log in form, with his username (email) and password.

## 3. Make a research

This functionality works either the user is logged in or not. He has to fill in the search bar (at the top of the page or the one right at the beginning of the home page) with a keyword.\
ex. "Banana" will give him every product that contains the word in it name, ordered by their nutriscores (from E to A).

## 4. Select a product

Once the query is done, the application returns a bunch of products that match. The user can consult the details of each one of them and just has to choose which one he wants to substitute.

## 5. Select and save a substitute

The application returns products of the same category but only those with better or equivalent Nutriscore.\
Here again, the user can consult the nutritionals details and have access to the product card in the Open Food Facts website.
By clicking on the save icon, the product will be saved as a favorite for the user. If he's not logged in, the user is redirected to the login page.

## 6. Consult your favorites in your account

By clicking on the carot icon in the navbar, the user has access to all his favorites products and consult the details of every one of them.

## 7. Log out of your account
Once the user is connected to his account, he can at every moment log out of his account by clicking on the disconnect icon.