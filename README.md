# Nexford_BAN_Web_Dev


## README

## WEB DEVELOPMENT WITH FLASK, MONGOBD & AWS

This ia a web development project for a company in Washington Dc that want to launch a new product in the healthcare industry. The task is to develop a survey tool for collecting data of participants with an objective to analyze their income in preparation of the launch of the company.



## INSTRUCTIONS

We will perform the following tasks:

1.	Web Development with Flask:

o	Create a simple webpage using Flask to collect user data.

2.	Data Storage with MongoDB:

o	Store user details, including Age, Gender, Total Income, and Expenses, in MongoDB.
o	Use checkboxes for expense categories (utilities, entertainment, school fees, shopping, healthcare), each with a corresponding textbox to insert amounts spent.

3.	Data Processing with Python or R:

o	Create a Python or R class named "User."
o	Loop through the collected data and store it in a CSV file.
o	Load the CSV file into a Jupyter notebook.

4.	Data Visualization:

o	Perform the following visualizations in your Jupyter notebook:
	Show the ages with the highest income.
	Show the gender distribution across spending categories.
	Export the charts for use in a PowerPoint presentation for client use.

5.	Deployment on AWS:

o	Host the Flask application on Amazon Web Services (AWS).




## INSTALLATION

Install Flask and Mongodb
```bash
pip install Flask

pip install pymongo
```

## Running Python


#Steps To Using Flask and Mongobd in Python:

To create using flask to collect user data
```bash
from flask import Flask, render_template, request, redirect
import pymongo
```

HTML code for webpage
```bash
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Survey Tool</title>
</head>
```

Storage of user details
```bash
@app.route('/submit', methods=['POST'])
```

Code Excecution
```bash
Running on http://127.0.0.1:5000
```

To create class
```bash
import csv
from pymongo import MongoClient

class User:
    def __init__(self, db_name, collection_name):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
```

Store data in csv
```bash
user = User("survey_data", "responses")
user.export_to_csv("survey_data.csv")
```

Import all libraries for visulaization
```bash
import pandas as pd
import matplotlib.pyplot as plt
```

## Lessons  

The instaltion of flask and mongodb into vscode to create a simple webpage application code to collect users data and importing pymongo to store user details  i.e Age, Gender, Total Income, and Expenses, in MongoDB. Also, wtiting HTML codes and applying the use checkboxes for expense categories (utilities, entertainment, school fees, shopping, healthcare), each with a corresponding textbox to insert amount spent.

Data processing was written in jupyternotbook to create a loop through the colected data and store it in a CSV file and visualizations to shiw all the attributes of the data stored in the csv file.

The flask application is then Hosted into AWS by launching an instance. After which it was deployed into windows terminal 



Connect to your EC2 instance using SSH:
```bash
ssh -i "C:\Users\HP ENVY\Downloads\windows.pem" ubuntu@13.60.238.130
```

Update the package list and install Python, Flask, and other necessary tools:
```bash
sudo apt update
sudo apt install python3-pip python3-dev nginx git
pip3 install flask pymongo
```

Clone Your Flask app hosted on github
```bash
https://github.com/Raolah/Nexford_BAN_Web_Dev/blob/f46351ce41e86d05b510d4083de1bf6be8b2ae7a/Flask.py
```

Move into the directory containg the flask app
```bash
cd Nexford_BAN_Web_Dev
```

Run Flask app
```bash
flask run --host=0.0.0.0:5000
```

To run the flask app, open this URL in a browser:
http://127.0.0.1:5000
## Requirements

* Python 3.x
* Flask
* Mongodb
* HTML
* AWS
* Windows Terminal
* PuTTY
