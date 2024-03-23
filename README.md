
# Flask CRUD API Project

## About

This project, part of the **Post Graduation Degree in Artificial Intelligence and Machine Learning** program offered by **[XP EDUCAÇÃO](https://www.xpeducacao.com.br/)**, serves as a practical exercise for mastering CRUD (Create, Read, Update, Delete) operations using Flask, a micro web framework for Python, and SQLite3 as the database. It aims to demonstrate the implementation of a RESTful API with endpoints to perform basic CRUD operations on a user database.

## Objective

The primary objective of this project is to reinforce understanding and implementation of CRUD operations in a Flask application. By breaking down the project into separate components such as controllers, routes, and `app.py`, it provides a structured approach to building a real-life API with CRUD functionalities.

## Features

-   List all users
-   Show details of a single user
-   Create a new user
-   Update user details
-   Delete a user

## Project Structure
-   **controllers/**: Contains controller functions responsible for handling business logic.
-   **routes/**: Defines routes and endpoints for CRUD operations.
-   **app.py**: Main application file responsible for initializing Flask app and connecting routes.
-   **database.py**: Manages SQLite3 database connection and operations.
-   **schema.sql**: Defines the database schema.
-   **README.md**: You're reading it!

## Usage
  
**1. Clone the repository:** ```bash git clone git@github.com:thiagohrcosta/flask-app.gitr_id

**2.  vigate to the project directory:**  `cd flask-app` 

**3.  Install dependencies:**  `pip install -r requirements.txt` 

**4.  Initialize the SQLite3 database:** `python database.py` 

**5.  Run the application**: `python app.py` 

**6.  Access the API endpoints:**
    
    **   List all users: ** `GET /users`
    **   Show user details: ** `GET /users/{user_id}`
    **   Create a new user: ** `POST /users/create`
    **   Update user details: ** `PUT /users/update/{user_id}/edit`
    **   Delete a user: ** `DELETE /users/delete/{user_id}````
