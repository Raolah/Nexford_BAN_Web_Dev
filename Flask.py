#create a webpage using flask to collect user data
from flask import Flask, render_template, request, redirect
import pymongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Process form data and store it in MongoDB
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')


#data storage of store user details with mongodb
@app.route('/submit', methods=['POST'])
def submit():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["survey_data"]
    collection = db["responses"]

    # Collect form data
    age = request.form['age']
    gender = request.form['gender']
    income = request.form['income']
    expenses = {
        "Utilities": request.form.get('utilities'),
        "Entertainment": request.form.get('entertainment'),
        "School Fees": request.form.get('school_fees'),
        "Shopping": request.form.get('shopping'),
        "Healthcare": request.form.get('healthcare')
    }

    # Store data in MongoDB
    collection.insert_one({
        "Age": age,
        "Gender": gender,
        "Total Income": income,
        "Expenses": expenses
    })

    return redirect('/')
