# Flask API Application Documentation

This is a simple Flask-based REST API application that interacts with a database to manage data related to people. The application provides endpoints to fetch, create, update, and delete records of people.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Project Structure](#project-structure)
4. [Configuration](#configuration)
5. [Setting Up the Application](#setting-up-the-application)
6. [Running the Application](#running-the-application)
7. [API Endpoints](#api-endpoints)
   1. [GET /](#get-)
   2. [GET /getAllData](#get-alldata)
   3. [GET /fetchData](#get-fetchdata)
   4. [GET /getData/<int:id>](#get-getdataintid)
   5. [PUT /editData/<int:id>](#put-editdataintid)
   6. [DELETE /deleteData/<int:id>](#delete-deletedataintid)
8. [Error Handling](#error-handling)
9. [Example Usage](#example-usage)
10. [License](#license)

---

## Introduction

This is a simple Flask-based REST API that allows users to manage people data (like name, height, mass, hair color, etc.) stored in a database. It supports **CRUD operations** (Create, Read, Update, Delete) for people records and can fetch data from an external API (SWAPI - Star Wars API) to populate the database.

---

## Configuration

### Clone the Repository

First, clone the project repository to your local machine using Git:

```bash
git clone https://github.com/onirstudy/SWAPI.git
cd SWAPI
```

---
## Requirements

Follow these steps to set up and run the Flask application on your local machine.

Before you begin, ensure you have the following installed:

- Python 3.x
- Flask
- SQLAlchemy
- Requests

To install the dependencies, run:

```bash
pip install -r requirements.txt
```

```bash
 python app.py
```

```bash
python crudtests.py
```

### Explanation:
- **First Command (`pip install -r requirements.txt`)**: This command installs all the dependencies listed in your `requirements.txt` file.
- **Second Command (`python app.py`)**: This starts the main application by executing the `app.py` file.
- **Third Command (`python crudtests.py`)**: This runs the tests defined in the `crudtests.py` file.

Each command is enclosed in its own code block, making the instructions clear and easy to follow when viewed in the `README.md` file.

---
# SWAPI

### Description

SWAPI is a simple Flask application that interacts with a database using SQLAlchemy to provide data from the Star Wars API.

### Project Structure

The project directory structure is as follows:


📁SWAPI

    📁.venv
    ├── app.py                   # Main Flask application
    ├── crudtests.py             # Tests for CRUD functionality
    ├── deletetestcase.py        # Tests for only deleteTestCase functionality
    ├── config.py                # Configuration file for Flask and database
    ├── models.py                # SQLAlchemy models for database interaction
    ├── templates/
    │   └── index.html           # HTML template for the index page
    ├── requirements.txt         # Python dependencies
    └── README.md                # Documentation for the project

---

## Running the Application

Once you have set up the application, you can run it locally by following these steps:

### 1. Start the Flask Application

To run the Flask app, use the following command:

```bash
python app.py
```

---

##  API Endpoints

Here are the full URLs for the endpoints:

    GET http://127.0.0.1:5000/ 
    (Renders the index.html page)

    GET http://127.0.0.1:5000/getAllData 
    (Fetches all data from the database)

    GET http://127.0.0.1:5000/fetchData  
    (Fetches data from the external API and stores it in the database)

    PUT http://127.0.0.1:5000/editData/<int:id>  
    (Edits a person's data by their ID)
 
    GET http://127.0.0.1:5000/getData/<int:id>   
    (Gets a person's data by their ID)

    DELETE http://127.0.0.1:5000/deleteData/<int:id> 
    (Deletes a person from the database by their ID)

```bash
   http://127.0.0.1:5000/
```
```bash
   http://127.0.0.1:5000/getAllData
```
```bash
   http://127.0.0.1:5000/fetchData
```
```bash
   http://127.0.0.1:5000/editData/<int:id>
```
```bash
   http://127.0.0.1:5000/getData/<int:id>
```
  (Deletes a person from the database by their ID)
```bash
   http://127.0.0.1:5000/deleteData/<int:id>
```

