# SIMPLE FLASK REST API

## Description

This project imitates an online store where clients can create a store , add items into the store including prices for each created item. Clients are also able to create accounts with the ability to login and logout

## Implementation

This project is implemented using flask, and is a REST API for a store


## Installation

```
pip install -r requirements.txt

```

## Run

```
python app.py

```
then go to [http://localhost:5000/stores](http://localhost:5000/stores) to get a list of all stores in the database

# Heroku
The project is also hosted on heroku --> [https://flask-api-api.herokuapp.com/stores](https://flask-api-api.herokuapp.com/stores)
 ´´´ <a href="/docs" class="btn btn-primary btn-md">Authentication</a> ´´´

## Project Structure

├───app.py # main app.py file to be called to start server for web app
|___README.md
├───requirements.txt   # File of pip install statements for your app
├───migrations    # folder created for migrations by calling
├───myproject   # main project folder, sub-components will be in separate folders
│   │   data.sqlite
│   │   models.py
│   │   __init__.py
│   │
│   ├───accounts
│   │   │   auth.py
│   │   │   models.py
|   |   |   views.py
│   │     
│   │
|   |
│   ├───items
│   │   │   models.py
│   │   │   views.py
│   │   
|   |
|   |
│   │___resources
│   │   │    item.py
│   │   │    register.py
│   │   │    store.py
│   │   
|   |
|   |
│   │___store
│   │   │    models.py
│   │   │    views.py
│   │   │    
