# E-Commerce

This is my submission for Microsoft Engage programme 2022.  I have built an E-Commerce website called Fashaholic, that makes use of recommendation algorithms which models people's preferences and behaviour.I have used HTML, CSS, Javascript  and Bootrap for my frontend and Django framework for my backend. I have used Django's default database Sqlite for storing data. I have also deployed the project on pythonanywhere.com. The project can be viewed live on this domain https://nehaproject.pythonanywhere.com/

Directory Layout
=================

Django E-commerce Website App's directory structure looks as follows::

    E-commerce/
        |---requirements.txt
        |---readme.md
        |---Fashaholic
                 |---core
                 |---djangoecommerce
                 |---media
                 |---static_in_env
                 |---templates
                 |---.env
                 |---db.sqlite3
                 |---manage.py

Usage
======

I recommend you to have Anaconda distribution of python 3.8 on your machine.

#Virtual environment creation and activation
    
    $ conda create --name envName python=3.8
    $ activate envName

#Cloning the project, installing dependencies and project navigation
    
    $ git clone https://github.com/neha-nellai/E-Commerce
    $ cd E-Commerce
    $ pip install -r requirements.txt
    $ cd Fashaholic

#Getting started

Finally, you have to make migrations to get the app started and create a new superuser to interact with the admin dashboard.

    $ python manage.py migrate
    $ python manage.py createsuperuser --user <username> --email <email>

So after successful completion of these you are ready to run the application by the following command:

    $ python manage.py runserver

Recommendation algorithms
==========================

+ Recommendations for You section
  The recommendations for you section is displayed only when the user is logged in to show personalised recommendations to the user. It makes use of user      collaborative filtering method - which is based on the premise that similar users have similar preferences. It identifies similar users based on products    they have liked, therefore this section starts showing relevant recommendations only after a user has liked a product that has already been previously       liked by some other user

+ Trending Products
  This is a weighted recommendation system based on user clicks. Positive weights are given for user actions like viewing a product, liking a product, adding to     cart and placing an order and negative weights for  unliking a product, removing a product from cart and requesting refund. Product with highest   weights are    sorted and shown in the trending products section. These recommendations will dynamically change depending on the users actions on the     website.

+ Popular Products
  This utilises python's Tim sort which is a hybrid of merge and insertion sort. It sorts the products in descending order of maximum likes and the top 4     most liked product are displayed in this section.

+ Similar Products section
  The similar products section on item detail view page displays products similar to the product currently being viewed by the user. I have made use of an     NLP library to extract keywords from the product description to get a bag of words, which are then compared to find similar products. 


Website Features
=================
+ User Authentication - User sign-up, login, logout, password reset
+ Filtering by Category - Kid's wear, Women's wear and Men's wear
+ Searching Items 
+ Adding & Removing Items From/To The Cart
+ Add Likes To Product
+ Cart Management
+ Applying Coupons to get discount
+ Checkout and Payment 
+ Order History
+ Request Refund
+ Customized Default Django Admin Dashboard

* I used a free template from mdbootstrap. I also used the Flipkart E-Commerce dataset from Kaggle and preprocessed the data using Microsoft Excel. I then imported the data from Excel into my Sqlite database to populate the product details.
